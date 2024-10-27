def moore_automaton(input_sequence):
    state = 'Q0'  # Estado inicial
    output_sequence = []  # Lista para almacenar la salida

    for bit in input_sequence:
        if state == 'Q0':
            if bit == '0':
                output_sequence.append('0')  # Emitir '0'
                state = 'Q0'
            elif bit == '1':
                output_sequence.append('1')  # Emitir '1'
                state = 'Q1'

        elif state == 'Q1':
            if bit == '0':
                output_sequence.append('0')  # Emitir '0'
                state = 'Q0'
            elif bit == '1':
                output_sequence[-1] = '0'  # Reemplaza el último '1' por '0'
                output_sequence.append('0')  # Emitir el segundo '0'
                state = 'Q0'  # Vuelve al estado inicial

    return ''.join(output_sequence)

# Ejemplo de uso:
input_sequence = "11011001"
output_sequence = moore_automaton(input_sequence)
print(f"Entrada: {input_sequence}")
print(f"Salida:  {output_sequence}")
