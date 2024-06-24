#!/usr/bin/env bash

cat <<'EOF'
$$$$$$$$\ $$$$$$$$\ $$\                           
\____$$  |\__$$  __|$$ |                          
    $$  /    $$ |   $$$$$$$\   $$$$$$\  $$$$$$$\  
   $$  /     $$ |   $$  __$$\ $$  __$$\ $$  __$$\ 
  $$  /      $$ |   $$ |  $$ |$$ /  $$ |$$ |  $$ |
 $$  /       $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$ |
$$$$$$$$\    $$ |   $$ |  $$ |\$$$$$$  |$$ |  $$ |
\________|   \__|   \__|  \__| \______/ \__|  \__|
                                                  
                                                  
                                                  
Copyright (C) 2020-2024 by RRYR7@Github, < https://github.com/RRYR7 >.
This file is part of < https://github.com/RRYR7/Koyeb > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/RRYR7/koyeb/blob/main/LICENSE >
All rights reserved.
EOF

gunicorn app:app --daemon && python -m Tepthon
