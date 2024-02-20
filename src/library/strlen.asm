; INPUT
;   rsi - null terminated string
; OUTPUT
;   rax - result

_strlen:
    push  rcx
    xor   rcx, rcx

_strlen_next:
    cmp   [rsi], byte 0
    jz    _strlen_null
    inc   rcx
    inc   rsi
    jmp   _strlen_next 

_strlen_null:
    mov rax, rcx
    pop rcx 
    ret
