; INPUT
;   rsi - null terminated string

_puts:
    push rax
    push rdi

    push rsi
    call _strlen
    pop rsi
    mov rdx, rax

    mov rax, 1      ; write syscall
    syscall

    pop rdi
    pop rax
    ret
