import sys
import re

def patch_addressbook():
    with open('src/addressbook.c', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    callbacks = [
        "addressbook_new_book_cb", "addressbook_new_vcard_cb", "addressbook_treenode_edit_cb",
        "addressbook_treenode_delete_cb", "addressbook_file_save_cb", "close_cb",
        "addressbook_copy_address_cb", "addressbook_paste_address_cb", "addressbook_new_address_cb",
        "addressbook_new_group_cb", "addressbook_new_folder_cb", "addressbook_compose_to_cb",
        "addressbook_edit_address_cb", "addressbook_delete_address_cb"
    ]

    new_lines = []
    in_array = False
    for line in lines:
        if line.startswith("static GtkItemFactoryEntry addressbook_entries[] =") or \
           line.startswith("static GtkItemFactoryEntry addressbook_tree_popup_entries[] =") or \
           line.startswith("static GtkItemFactoryEntry addressbook_list_popup_entries[] ="):
            in_array = True
            
        if in_array and line.startswith("};"):
            in_array = False
            
        if in_array and "{N_(" in line or ("NULL," in line and "COMPOSE_ENTRY" in line) or ("NULL," in line and "addressbook_" in line):
            # Check for each callback
            for cb in callbacks:
                if cb in line and f"(GtkItemFactoryCallback) {cb}" not in line:
                    line = line.replace(cb, f"(GtkItemFactoryCallback) {cb}")
            
            # Ensure it ends with exactly 6 elements
            # This is a bit tricky if the line continues, but most of these are single lines ending in }, or }
            if line.strip().endswith("},"):
                # Count commas to estimate fields. 
                # An easier way is just to replace the specific endings.
                line = line.replace(", 0, NULL},", ", 0, NULL, NULL},")
                line = line.replace(", COMPOSE_ENTRY_TO, NULL},", ", COMPOSE_ENTRY_TO, NULL, NULL},")
                line = line.replace(", COMPOSE_ENTRY_CC, NULL},", ", COMPOSE_ENTRY_CC, NULL, NULL},")
                line = line.replace(", COMPOSE_ENTRY_BCC, NULL},", ", COMPOSE_ENTRY_BCC, NULL, NULL},")
                line = line.replace(", \"<Separator>\"},", ", \"<Separator>\", NULL},")
                line = line.replace(", \"<Branch>\"},", ", \"<Branch>\", NULL},")
            elif line.strip().endswith("}"):
                # Last element in array
                line = line.replace(", 0, NULL}", ", 0, NULL, NULL}")
                line = line.replace(", COMPOSE_ENTRY_TO, NULL}", ", COMPOSE_ENTRY_TO, NULL, NULL}")
                line = line.replace(", COMPOSE_ENTRY_CC, NULL}", ", COMPOSE_ENTRY_CC, NULL, NULL}")
                line = line.replace(", COMPOSE_ENTRY_BCC, NULL}", ", COMPOSE_ENTRY_BCC, NULL, NULL}")
                line = line.replace(", \"<Separator>\"}", ", \"<Separator>\", NULL}")
                line = line.replace(", \"<Branch>\"}", ", \"<Branch>\", NULL}")
                
        new_lines.append(line)

    with open('src/addressbook.c', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Patched src/addressbook.c successfully.")

if __name__ == "__main__":
    patch_addressbook()
