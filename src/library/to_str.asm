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
