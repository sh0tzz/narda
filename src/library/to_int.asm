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
