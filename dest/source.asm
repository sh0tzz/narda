global _start

section .data
    NEWLINE db 10, 0
    L0 db "Kak se zoves: ", 0
    L2 db "Koliko imas godina: ", 0
    L4 db "Bok ", 0
    L5 db "Imas ", 0




section .bss
    INPUT_BUFFER resb 64
    ime resb 32
    godine resb 32


section .text
_start:
    mov rsi, L0
call _puts
mov rax, 0
mov rdi, 0
mov rsi, ime
mov rdx, 32
syscall
mov rsi, L2
call _puts
mov rax, 0
mov rdi, 0
mov rsi, godine
mov rdx, 32
syscall
mov rsi, L4
call _puts
mov rsi, ime
call _puts
mov rsi, L5
call _puts
mov rsi, godine
call _puts


    mov rax, 60
    mov rdi, 0
    syscall




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



_newl:
    push rsi
    mov rsi, NEWLINE
    call _puts
    pop rsi
    ret
