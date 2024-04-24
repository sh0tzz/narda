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
