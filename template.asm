global _start

section .text
_start:
    mov rsi, text
    call _puts

    mov rax, 60
    mov rdi, 0
    syscall

#LIBRARIES#

section .data
    text db "Hello", 10, 0

