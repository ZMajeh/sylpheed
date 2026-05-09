# Patch script for src/messageview.c
$file = "src/messageview.c"
$content = Get-Content $file -Raw

# Pattern for callback casts
$callbacks = @(
    "save_as_cb", "page_setup_cb", "print_cb", "close_cb", "copy_cb",
    "allsel_cb", "search_cb", "set_charset_cb", "view_source_cb",
    "show_all_header_cb", "compose_cb", "reply_cb", "reedit_cb",
    "addressbook_open_cb", "add_address_cb", "create_filter_cb", "about_cb"
)

foreach ($cb in $callbacks) {
    # Replace the callback function name with the casted version
    $pattern = "NULL, $cb"
    $replacement = "NULL, (GtkItemFactoryCallback) $cb"
    $content = $content -replace $pattern, $replacement
}

# Fix 6-field struct requirement
# Find patterns that end with 5 fields and add a trailing NULL
# Match: ..., 0, NULL}
$content = $content -replace ", 0, NULL\}", ", 0, NULL, NULL\}"
# Match: ..., "<ToggleItem>"}
$content = $content -replace ', "<ToggleItem>"}', ', "<ToggleItem>", NULL}'
# Match: ..., "<RadioItem>"}
$content = $content -replace ', "<RadioItem>"}', ', "<RadioItem>", NULL}'

Set-Content $file -Value $content
Write-Host "Patched $file"
