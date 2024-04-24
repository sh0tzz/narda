global _start

section .data
    NEWLINE db 10, 0
        L2 db "Unesi prvi broj: ", 0
    L3 db "Unesi drugi broj: ", 0




section .bss
    TEMP resb 64
    a resb 32
b resb 32


section .text
_start:
    mov rsi, L2
call _puts
mov rax, 0
mov rdi, 0
mov rsi, a
mov rdx, 32
syscall
mov rsi, L3
call _puts
mov rax, 0
mov rdi, 0
mov rsi, b
mov rdx, 32
syscall
mov rsi, a
call _to_int
mov rsi, b
call _to_int
mov rsi, a
call _puts
call _newl
mov rsi, b
call _puts
call _newl
mov rdi, [a]
call _to_str
mov rsi, a
call _puts
call _newl
mov rsi, b
call _puts
call _newl


    mov rsi, TEMP
    call _puts

    mov rax, 60
    mov rdi, 0
    syscall




; memcpy(dst, src, size)
; rdi = dst, rsi = src, rcx = size
_memcpy:
    test rcx, rcx          ; Check if size is zero
    jz .done

.loop:
    mov rdx, [rsi]         ; Load 64 bits from src to rdx
    mov [rdi], rdx         ; Store 64 bits from rdx to dst
    add rdi, 8             ; Move dst pointer by 8 bytes
    add rsi, 8             ; Move src pointer by 8 bytes
    sub rcx, 8             ; Decrease size by 8 bytes
    jnz .loop              ; Loop until size is zero
.done:
    xor rdi, rdi
    ret



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



; INPUT
;   rsi - source

_to_int:
    push rax
    push rdx
    push rcx

    xor rax, rax
    xor rcx, rcx

parse_loop:
    movzx   rdx, byte [rsi + rcx]   ; Load the current character into rdx
    cmp     rdx, 0                  ; Check if it's null terminator
    je      done_parse              ; If null terminator, we're done parsing
    cmp     rdx, 10                 ; Check if it's a line break character
    je      skip_char               ; If line break, skip this character
    sub     rdx, '0'                ; Convert ASCII digit to numeric value
    imul    rax, rax, 10            ; Multiply current result by 10
    add     rax, rdx                ; Add the current digit to the result
skip_char:
    inc     rcx                     ; Move to the next character
    jmp     parse_loop

done_parse:
    ; At this point, rax contains the integer value of the string
    ; You can use rax for further operations or output
    mov [rsi], rax

    pop rcx
    pop rdx
    pop rax
    ret



_to_str:
    ; Arguments:
    ; rdi: 64-bit integer to convert

    ; Save registers
    push rbx
    push rsi
    push rdx

    ; Initialize variables
    mov rsi, TEMP + 32       ; Pointer to the buffer to store the string
    mov rbx, 10         ; Divisor for division by 10
    mov rcx, 0          ; Initialize digit counter

convert_loop:
    mov rax, rdi        ; Move the integer to rax
    xor rdx, rdx        ; Clear rdx for division
    div rbx             ; Divide rax by 10, quotient in rax, remainder in rdx
    add dl, '0'         ; Convert remainder to ASCII
    dec rsi             ; Move buffer pointer back
    mov [rsi], dl       ; Store ASCII digit in buffer
    inc rcx             ; Increment digit counter
    test rdi, rdi       ; Check if quotient is zero
    jnz convert_loop    ; If not zero, continue loop

    ; Move the string to the beginning of the buffer
    mov rsi, TEMP       ; Reset pointer to the start of the buffer
    mov rdi, TEMP       ; Destination for moving the string
    add rdi, rcx        ; Move the destination pointer to the end of the string
    mov rcx, rcx        ; Number of bytes to move (excluding null terminator)
    rep movsb           ; Move the string to the beginning of the buffer

    ; Add null terminator at the end of the string
    mov byte [rsi - 1], 0

    ; Restore registers
    pop rdx
    pop rsi
    pop rbx
    ret



_newl:
    push rsi
    mov rsi, NEWLINE
    call _puts
    pop rsi
    ret
