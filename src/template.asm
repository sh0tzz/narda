global _start

section .data
    NEWLINE db 10, 0
    #LITERALS#



section .bss
    INPUT_BUFFER resb 64
    #VARIABLES#

section .text
_start:
    #MAIN#

    mov rax, 60
    mov rdi, 0
    syscall

#LIBRARIES#







