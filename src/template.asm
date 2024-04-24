global _start

section .data
    NEWLINE db 10, 0
    #LITERALS#



section .bss
    TEMP resb 64
    #VARIABLES#

section .text
_start:
    #MAIN#

    mov rsi, TEMP
    call _puts

    mov rax, 60
    mov rdi, 0
    syscall

#LIBRARIES#







