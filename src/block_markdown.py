
def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n\n")
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        blocks.append(line)
    return blocks

def block_to_block_type(block):
    #Simple block types
    headers = {
        "# ": "head1",
        "## ": "head2",
        "### ": "head3",
        "#### ": "head4",
        "##### ": "head5",
        "######": "head6",
    }
    for key in headers.keys():
        if block.startswith(key):
            return headers[key]
    if block.startswith("```"):
        if block.endswith("```"):
            return "code"
    
    #More complex block types
    prev_block_type = "init"
    for i, line in enumerate(block.splitlines()):
        all_lines = False
        
        #Block types
        if line.startswith("> "):
            block_type = "quote"
            all_lines = True
        if line.startswith("* ") or line.startswith("- "):
            block_type = "ulist"
            all_lines = True
        if line.startswith(f"{i+1}."):
            block_type = "olist"
            all_lines = True

        #Verify all lines are matching.
        if prev_block_type != "init":
            if block_type != prev_block_type:
                all_lines = False
        if all_lines == False:
            break
        prev_block_type = block_type

    if all_lines == True:
        return(block_type)
    return("par")

def quote_to_html(block):
    
