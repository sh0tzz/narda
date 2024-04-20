global _start

section .data
    NEWLINE db 10, 0
    #LITERALS#



section .bss
    INPUT_BUFFER resb 64


section .text
_start:
    #MAIN#

    mov rsi, INPUT_BUFFER
    call _puts
    
    mov rax, 60
    mov rdi, 0
    syscall

#LIBRARIES#







