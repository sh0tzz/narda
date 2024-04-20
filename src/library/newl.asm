_newl:
    push rsi
    mov rsi, NEWLINE
    call _puts
    pop rsi
    ret
