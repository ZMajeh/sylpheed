import sys

def patch_compose():
    with open('src/compose.c', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the start and end indices
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if line.startswith("static GtkItemFactoryEntry compose_popup_entries[] ="):
            start_idx = i
        if start_idx != -1 and line.startswith("};") and i > 740:
            end_idx = i
            break

    if start_idx == -1 or end_idx == -1:
        print("Could not find the bounds.")
        return

    clean_content = """static GtkItemFactoryEntry compose_popup_entries[] =
{
	{N_("/_Open"),          NULL, (GtkItemFactoryCallback) compose_attach_open_cb, 0, NULL, NULL},
	{N_("/---"),            NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_Add..."),        NULL, (GtkItemFactoryCallback) compose_attach_cb, 0, NULL, NULL},
	{N_("/_Remove"),        NULL, (GtkItemFactoryCallback) compose_attach_remove_selected, 0, NULL, NULL},
	{N_("/---"),            NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_Properties..."), NULL, (GtkItemFactoryCallback) compose_attach_property, 0, NULL, NULL}
};

static GtkItemFactoryEntry compose_entries[] =
{
	{N_("/_File"),				NULL, NULL, 0, "<Branch>", NULL},
	{N_("/_File/_Send"),			"<shift><control>E",
						(GtkItemFactoryCallback) compose_send_cb, 0, NULL, NULL},
	{N_("/_File/Send _later"),		"<shift><control>S",
						(GtkItemFactoryCallback) compose_send_later_cb,  0, NULL, NULL},
	{N_("/_File/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_File/Save to _draft folder"),	"<shift><control>D", (GtkItemFactoryCallback) compose_draft_cb, 0, NULL, NULL},
	{N_("/_File/Save and _keep editing"),	"<control>S", (GtkItemFactoryCallback) compose_draft_cb, 1, NULL, NULL},
	{N_("/_File/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_File/_Attach file"),		"<control>M", (GtkItemFactoryCallback) compose_attach_cb,      0, NULL, NULL},
	{N_("/_File/_Insert file"),		"<control>I", (GtkItemFactoryCallback) compose_insert_file_cb, 0, NULL, NULL},
	{N_("/_File/Insert si_gnature"),	"<control>G", (GtkItemFactoryCallback) compose_insert_sig_cb,  0, NULL, NULL},
	{N_("/_File/A_ppend signature"),	"<shift><control>G", (GtkItemFactoryCallback) compose_insert_sig_cb,  1, NULL, NULL},
	{N_("/_File/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_File/_Close"),			"<control>W", (GtkItemFactoryCallback) compose_close_cb, 0, NULL, NULL},

	{N_("/_Edit"),				NULL, NULL, 0, "<Branch>", NULL},
	{N_("/_Edit/_Undo"),			"<control>Z", (GtkItemFactoryCallback) compose_undo_cb, 0, NULL, NULL},
	{N_("/_Edit/_Redo"),			"<control>Y", (GtkItemFactoryCallback) compose_redo_cb, 0, NULL, NULL},
	{N_("/_Edit/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_Edit/Cu_t"),			"<control>X", (GtkItemFactoryCallback) compose_cut_cb,    0, NULL, NULL},
	{N_("/_Edit/_Copy"),			"<control>C", (GtkItemFactoryCallback) compose_copy_cb,   0, NULL, NULL},
	{N_("/_Edit/_Paste"),			"<control>V", (GtkItemFactoryCallback) compose_paste_cb,  0, NULL, NULL},
	{N_("/_Edit/Paste as _quotation"),	NULL, (GtkItemFactoryCallback) compose_paste_as_quote_cb, 0, NULL, NULL},
	{N_("/_Edit/Select _all"),		"<control>A", (GtkItemFactoryCallback) compose_allsel_cb, 0, NULL, NULL},
	{N_("/_Edit/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_Edit/_Wrap current paragraph"),	"<control>L", (GtkItemFactoryCallback) compose_wrap_cb, 0, NULL, NULL},
	{N_("/_Edit/Wrap all long _lines"),	"<control><alt>L", (GtkItemFactoryCallback) compose_wrap_cb, 1, NULL, NULL},
	{N_("/_Edit/Aut_o wrapping"),		"<shift><control>L", (GtkItemFactoryCallback) compose_toggle_autowrap_cb, 0, "<ToggleItem>", NULL},

	{N_("/_View"),				NULL, NULL, 0, "<Branch>", NULL},
	{N_("/_View/_To"),			NULL, (GtkItemFactoryCallback) compose_toggle_to_cb     , 0, "<ToggleItem>", NULL},
	{N_("/_View/_Cc"),			NULL, (GtkItemFactoryCallback) compose_toggle_cc_cb     , 0, "<ToggleItem>", NULL},
	{N_("/_View/_Bcc"),			NULL, (GtkItemFactoryCallback) compose_toggle_bcc_cb    , 0, "<ToggleItem>", NULL},
	{N_("/_View/_Reply-To"),		NULL, (GtkItemFactoryCallback) compose_toggle_replyto_cb, 0, "<ToggleItem>", NULL},
	{N_("/_View/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_View/_Followup-To"),		NULL, (GtkItemFactoryCallback) compose_toggle_followupto_cb, 0, "<ToggleItem>", NULL},
	{N_("/_View/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_View/R_uler"),			NULL, (GtkItemFactoryCallback) compose_toggle_ruler_cb, 0, "<ToggleItem>", NULL},
	{N_("/_View/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_View/_Attachment"),		NULL, (GtkItemFactoryCallback) compose_toggle_attach_cb, 0, "<ToggleItem>", NULL},
	{N_("/_View/---"),			NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_View/_Customize toolbar..."),	NULL, (GtkItemFactoryCallback) compose_customize_toolbar_cb, 0, NULL, NULL},
	{N_("/_View/---"),			NULL, NULL, 0, "<Separator>", NULL},

#define ENC_SEPARATOR \\
	{N_("/_View/Character _encoding/---"),		NULL, NULL, 0, "<Separator>", NULL}
#define ENC_ACTION(action) \\
	NULL, (GtkItemFactoryCallback) set_charset_cb, action, NULL, NULL

	{N_("/_View/Character _encoding"),	NULL, NULL, 0, "<Branch>", NULL},
	{N_("/_View/Character _encoding/_Auto detect"),
			NULL, (GtkItemFactoryCallback) compose_set_encoding_cb, C_AUTO, "<RadioItem>", NULL},
	{N_("/_View/Character _encoding/---"),	NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_View/Character _encoding/7bit ascii (US-ASC_II)"),
	 {ENC_ACTION(C_US_ASCII)}},
	{N_("/_View/Character _encoding/Unicode (_UTF-8)"),
	 {ENC_ACTION(C_UTF_8)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Western European (ISO-8859-_1)"),
	 {ENC_ACTION(C_ISO_8859_1)}},
	{N_("/_View/Character _encoding/Western European (ISO-8859-15)"),
	 {ENC_ACTION(C_ISO_8859_15)}},
	{N_("/_View/Character _encoding/Western European (Windows-1252)"),
	 {ENC_ACTION(C_WINDOWS_1252)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Central European (ISO-8859-_2)"),
	 {ENC_ACTION(C_ISO_8859_2)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/_Baltic (ISO-8859-13)"),
	 {ENC_ACTION(C_ISO_8859_13)}},
	{N_("/_View/Character _encoding/Baltic (ISO-8859-_4)"),
	 {ENC_ACTION(C_ISO_8859_4)}},
	{N_("/_View/Character _encoding/Baltic (Windows-1257)"),
	 {ENC_ACTION(C_WINDOWS_1257)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Greek (ISO-8859-_7)"),
	 {ENC_ACTION(C_ISO_8859_7)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Arabic (ISO-8859-_6)"),
	 {ENC_ACTION(C_ISO_8859_6)}},
	{N_("/_View/Character _encoding/Arabic (Windows-1256)"),
	 {ENC_ACTION(C_CP1256)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Hebrew (ISO-8859-_8)"),
	 {ENC_ACTION(C_ISO_8859_8)}},
	{N_("/_View/Character _encoding/Hebrew (Windows-1255)"),
	 {ENC_ACTION(C_CP1255)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Turkish (ISO-8859-_9)"),
	 {ENC_ACTION(C_ISO_8859_9)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Cyrillic (ISO-8859-_5)"),
	 {ENC_ACTION(C_ISO_8859_5)}},
	{N_("/_View/Character _encoding/Cyrillic (KOI8-_R)"),
	 {ENC_ACTION(C_KOI8_R)}},
	{N_("/_View/Character _encoding/Cyrillic (KOI8-U)"),
	 {ENC_ACTION(C_KOI8_U)}},
	{N_("/_View/Character _encoding/Cyrillic (Windows-1251)"),
	 {ENC_ACTION(C_CP1251)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Japanese (ISO-2022-_JP)"),
	 {ENC_ACTION(C_ISO_2022_JP)}},
	{N_("/_View/Character _encoding/Japanese (ISO-2022-JP-2)"),
	 {ENC_ACTION(C_ISO_2022_JP_2)}},
	{N_("/_View/Character _encoding/Japanese (_EUC-JP)"),
	 {ENC_ACTION(C_EUC_JP)}},
	{N_("/_View/Character _encoding/Japanese (_Shift__JIS)"),
	 {ENC_ACTION(C_SHIFT_JIS)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Simplified Chinese (_GB2312)"),
	 {ENC_ACTION(C_GB2312)}},
	{N_("/_View/Character _encoding/Simplified Chinese (GBK)"),
	 {ENC_ACTION(C_GBK)}},
	{N_("/_View/Character _encoding/Traditional Chinese (_Big5)"),
	 {ENC_ACTION(C_BIG5)}},
	{N_("/_View/Character _encoding/Traditional Chinese (EUC-_TW)"),
	 {ENC_ACTION(C_EUC_TW)}},
	{N_("/_View/Character _encoding/Chinese (ISO-2022-_CN)"),
	 {ENC_ACTION(C_ISO_2022_CN)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Korean (EUC-_KR)"),
	 {ENC_ACTION(C_EUC_KR)}},
	{N_("/_View/Character _encoding/Korean (ISO-2022-KR)"),
	 {ENC_ACTION(C_ISO_2022_KR)}},
	ENC_SEPARATOR,
	{N_("/_View/Character _encoding/Thai (TIS-620)"),
	 {ENC_ACTION(C_TIS_620)}},
	{N_("/_View/Character _encoding/Thai (Windows-874)"),
	 {ENC_ACTION(C_WINDOWS_874)}},

#undef ENC_SEPARATOR
#undef ENC_ACTION

	{N_("/_Tools"),			NULL, NULL, 0, "<Branch>", NULL},
	{N_("/_Tools/_Address book"),	"<shift><control>A", (GtkItemFactoryCallback) compose_address_cb , 0, NULL, NULL},
	{N_("/_Tools/_Template"),	NULL, NULL, 0, "<Branch>", NULL},
	{N_("/_Tools/---"),		NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_Tools/Edit with e_xternal editor"),
					"<shift><control>X", (GtkItemFactoryCallback) compose_ext_editor_cb, 0, NULL, NULL},
	{N_("/_Tools/---"),		NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_Tools/Request _disposition notification"),	NULL, (GtkItemFactoryCallback) compose_toggle_mdn_cb   , 0, "<ToggleItem>", NULL},
	{N_("/_Tools/---"),		NULL, NULL, 0, "<Separator>", NULL},
	{N_("/_Tools/PGP Si_gn"),	NULL, (GtkItemFactoryCallback) compose_toggle_sign_cb   , 0, "<ToggleItem>", NULL},
	{N_("/_Tools/PGP _Encrypt"),	NULL, (GtkItemFactoryCallback) compose_toggle_encrypt_cb, 0, "<ToggleItem>", NULL},

	{N_("/_Help"),			NULL, NULL, 0, "<Branch>", NULL},
	{N_("/_Help/_About"),		NULL, (GtkItemFactoryCallback) about_show, 0, NULL, NULL}
};
"""
    new_lines = lines[:start_idx] + [clean_content] + lines[end_idx+1:]
    
    with open('src/compose.c', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Patched successfully.")

if __name__ == "__main__":
    patch_compose()
