import turtle
import time
import random

CELL_SIZE = 45
GRID_X = -110
GRID_Y = 220
SPEED_MULTIPLIER = 1

def setup_screen():
    screen = turtle.Screen()
    screen.title("Cipher Animations - Main Menu")
    screen.setup(width=900, height=850)
    screen.bgcolor("#ffffff")
    screen.tracer(0) 
    return screen

def draw_box(t, x, y, size, text, fill_color="white", text_color="black"):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    
    t.penup()
    t.goto(x + size / 2, y - size + 10)
    t.pencolor(text_color)
    t.write(text, align="center", font=("Arial", 14, "bold"))

def draw_polybius_grid(t):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for col in range(5):
        draw_box(t, GRID_X + col*CELL_SIZE, GRID_Y + CELL_SIZE, CELL_SIZE, str(col+1), "#eeeeee", "blue")
    
    for row in range(5):
        draw_box(t, GRID_X - CELL_SIZE, GRID_Y - row*CELL_SIZE, CELL_SIZE, str(row+1), "#eeeeee", "blue")
        
    for i, char in enumerate(alphabet):
        row = i // 5
        col = i % 5
        draw_box(t, GRID_X + col*CELL_SIZE, GRID_Y - row*CELL_SIZE, CELL_SIZE, char)

def get_coords(char):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    idx = alphabet.index(char)
    return (idx // 5) + 1, (idx % 5) + 1

def get_char(r, c):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    return alphabet[(r-1)*5 + (c-1)]

def show_intersection(t, r, c, char, final_color):
    row_y = GRID_Y - (r-1)*CELL_SIZE
    col_x = GRID_X + (c-1)*CELL_SIZE
    
    draw_box(t, GRID_X - CELL_SIZE, row_y, CELL_SIZE, str(r), "#ffa500", "white") 
    turtle.update()
    time.sleep(0.8 * SPEED_MULTIPLIER)
    
    draw_box(t, col_x, GRID_Y + CELL_SIZE, CELL_SIZE, str(c), "#ffa500", "white") 
    turtle.update()
    time.sleep(0.8 * SPEED_MULTIPLIER)
    
    draw_box(t, col_x, row_y, CELL_SIZE, char, final_color, "black")
    turtle.update()
    time.sleep(1.5 * SPEED_MULTIPLIER)
    
    draw_box(t, GRID_X - CELL_SIZE, row_y, CELL_SIZE, str(r), "#eeeeee", "blue")
    draw_box(t, col_x, GRID_Y + CELL_SIZE, CELL_SIZE, str(c), "#eeeeee", "blue")
    draw_box(t, col_x, row_y, CELL_SIZE, char, "white", "black")
    turtle.update()

def highlight_cell_simple(t, r, c, char, color):
    x = GRID_X + (c-1)*CELL_SIZE
    y = GRID_Y - (r-1)*CELL_SIZE
    draw_box(t, x, y, CELL_SIZE, char, color)
    turtle.update()
    time.sleep(1.0 * SPEED_MULTIPLIER) 
    draw_box(t, x, y, CELL_SIZE, char, "white") 
    turtle.update()

def update_status(writer_t, text):
    writer_t.clear()
    writer_t.penup()
    writer_t.goto(0, -30)
    writer_t.pencolor("darkred")
    writer_t.write(text, align="center", font=("Arial", 16, "bold"))
    turtle.update()

def animate_encryption(t, writer_t, word):
    t.clear()
    draw_polybius_grid(t)
    start_x = - (len(word) * 45) / 2 
    
    update_status(writer_t, f"1. Finding Coordinates for: {word}")
    time.sleep(1)
    
    rows, cols = [], []
    
    for i, char in enumerate(word):
        r, c = get_coords(char)
        
        draw_box(t, start_x + i*45, -70, 35, char, "#dddddd")
        turtle.update()
        time.sleep(0.5 * SPEED_MULTIPLIER)
        
        highlight_cell_simple(t, r, c, char, "#ffea00")
        
        draw_box(t, start_x + i*45, -120, 35, str(r), "lightblue")
        draw_box(t, start_x + i*45, -160, 35, str(c), "lightgreen")
        rows.append(r)
        cols.append(c)
        turtle.update()
        
    time.sleep(1 * SPEED_MULTIPLIER)
    
    update_status(writer_t, "2. Combining Rows and Columns into an array")
    combined = rows + cols
    start_comb_x = - (len(combined) * 35) / 2
    
    for i, num in enumerate(combined):
        color = "lightblue" if i < len(rows) else "lightgreen"
        draw_box(t, start_comb_x + i*35, -230, 35, str(num), color)
        turtle.update()
        time.sleep(0.3 * SPEED_MULTIPLIER)
        
    time.sleep(1.5 * SPEED_MULTIPLIER)
    
    update_status(writer_t, "3. Reading new pairs (Row, Column) for the ciphertext")
    ciphertext = ""
    for i in range(0, len(combined), 2):
        r, c = combined[i], combined[i+1]
        new_char = get_char(r, c)
        ciphertext += new_char
        
        draw_box(t, start_comb_x + i*35, -230, 35, str(r), "#ffea00")
        draw_box(t, start_comb_x + (i+1)*35, -230, 35, str(c), "#ffea00")
        turtle.update()
        
        show_intersection(t, r, c, new_char, "#00ff00")
        
        draw_box(t, start_x + (i//2)*45, -310, 35, new_char, "#00ff00")
        
        color1 = "lightblue" if i < len(rows) else "lightgreen"
        color2 = "lightblue" if i+1 < len(rows) else "lightgreen"
        draw_box(t, start_comb_x + i*35, -230, 35, str(r), color1)
        draw_box(t, start_comb_x + (i+1)*35, -230, 35, str(c), color2)
        turtle.update()
        
    update_status(writer_t, f"Encryption finished! Ciphertext: {ciphertext}")
    return ciphertext, combined

def animate_decryption(t, writer_t, ciphertext, original_len):
    t.clear()
    draw_polybius_grid(t)
    start_x = - (len(ciphertext) * 45) / 2
    
    update_status(writer_t, f"1. Finding coordinates for the ciphertext: {ciphertext}")
    time.sleep(1)
    
    combined = []
    
    start_comb_x = - (len(ciphertext) * 2 * 35) / 2
    for i, char in enumerate(ciphertext):
        r, c = get_coords(char)
        
        draw_box(t, start_x + i*45, -70, 35, char, "#dddddd")
        turtle.update()
        time.sleep(0.5 * SPEED_MULTIPLIER)
        
        highlight_cell_simple(t, r, c, char, "#ffea00")
        
        draw_box(t, start_comb_x + (i*2)*35, -130, 35, str(r), "#ffea00")
        draw_box(t, start_comb_x + (i*2+1)*35, -130, 35, str(c), "#ffea00")
        combined.extend([r, c])
        turtle.update()

    time.sleep(1.5 * SPEED_MULTIPLIER)
    
    update_status(writer_t, "2. Splitting array in half (Half 1=Rows, Half 2=Columns)")
    half = len(combined) // 2
    for i in range(half):
        draw_box(t, start_x + i*45, -200, 35, str(combined[i]), "lightblue")
        draw_box(t, start_x + i*45, -240, 35, str(combined[half+i]), "lightgreen")
        turtle.update()
        time.sleep(0.4 * SPEED_MULTIPLIER)
        
    time.sleep(1.5 * SPEED_MULTIPLIER)
    
    update_status(writer_t, "3. Reading coordinates top-down to find the word")
    for i in range(half):
        r = combined[i]
        c = combined[half+i]
        orig_char = get_char(r, c)
        
        draw_box(t, start_x + i*45, -200, 35, str(r), "#ffea00")
        draw_box(t, start_x + i*45, -240, 35, str(c), "#ffea00")
        
        show_intersection(t, r, c, orig_char, "#00ff00")
        
        draw_box(t, start_x + i*45, -310, 35, orig_char, "#00ff00")
        
        draw_box(t, start_x + i*45, -200, 35, str(r), "lightblue")
        draw_box(t, start_x + i*45, -240, 35, str(c), "lightgreen")
        turtle.update()
        
    update_status(writer_t, "Decryption finished! Original word restored.")

def animate_permutation_encryption(t, writer_t, word, key):
    t.clear()
    update_status(writer_t, f"PERMUTATION CIPHER: Encrypting the word '{word}'")
    time.sleep(1.5 * SPEED_MULTIPLIER)

    start_x = - (len(word) * 55) / 2 
    
    update_status(writer_t, "1. Each letter in the word has an original position (Index)")
    for i, char in enumerate(word):
        draw_box(t, start_x + i*55, 100, 45, char, "#dddddd")
        draw_box(t, start_x + i*55, 50, 45, str(i), "#eeeeee", "blue")
    turtle.update()
    time.sleep(2.5 * SPEED_MULTIPLIER)

    update_status(writer_t, f"2. The random key tells us which Index to take: {key}")
    for i, k in enumerate(key):
        draw_box(t, start_x + i*55, -50, 45, str(k), "#ffa500") 
    turtle.update()
    time.sleep(2.5 * SPEED_MULTIPLIER)

    update_status(writer_t, "3. Taking letters according to the key to create ciphertext")
    ciphertext = ""
    for new_pos, target_idx in enumerate(key):
        draw_box(t, start_x + new_pos*55, -50, 45, str(target_idx), "#ffea00")
        turtle.update()
        time.sleep(0.8 * SPEED_MULTIPLIER)
        
        char = word[target_idx]
        draw_box(t, start_x + target_idx*55, 100, 45, char, "#ffea00")
        turtle.update()
        time.sleep(1.2 * SPEED_MULTIPLIER)
        
        draw_box(t, start_x + new_pos*55, -150, 45, char, "#00ff00")
        ciphertext += char
        turtle.update()
        time.sleep(1 * SPEED_MULTIPLIER)
        
        draw_box(t, start_x + new_pos*55, -50, 45, str(target_idx), "#ffa500")
        draw_box(t, start_x + target_idx*55, 100, 45, char, "#dddddd")
        turtle.update()
        
    update_status(writer_t, f"Encryption finished! Ciphertext: {ciphertext}")
    return ciphertext

def animate_permutation_decryption(t, writer_t, ciphertext, key):
    t.clear()
    update_status(writer_t, f"PERMUTATION CIPHER: Decrypting '{ciphertext}'")
    time.sleep(1.5 * SPEED_MULTIPLIER)

    start_x = - (len(ciphertext) * 55) / 2
    
    update_status(writer_t, "1. We have the ciphertext and the key that was used")
    for i, char in enumerate(ciphertext):
        draw_box(t, start_x + i*55, 100, 45, char, "#dddddd")
        draw_box(t, start_x + i*55, 50, 45, str(key[i]), "#ffa500")
    turtle.update()
    time.sleep(2.5 * SPEED_MULTIPLIER)
    
    update_status(writer_t, "2. The key tells us where each letter RETURNS (Original index)")
    for i in range(len(ciphertext)):
        draw_box(t, start_x + i*55, -100, 45, "?", "#eeeeee", "gray")
    turtle.update()
    time.sleep(2 * SPEED_MULTIPLIER)

    plaintext_list = [""] * len(ciphertext)
    for current_pos, original_idx in enumerate(key):
        char = ciphertext[current_pos]
        
        draw_box(t, start_x + current_pos*55, 100, 45, char, "#ffea00")
        draw_box(t, start_x + current_pos*55, 50, 45, str(original_idx), "#ffea00")
        turtle.update()
        time.sleep(1.2 * SPEED_MULTIPLIER)
        
        draw_box(t, start_x + original_idx*55, -100, 45, char, "#00ff00")
        plaintext_list[original_idx] = char
        turtle.update()
        time.sleep(1 * SPEED_MULTIPLIER)
        
        draw_box(t, start_x + current_pos*55, 100, 45, char, "#dddddd")
        draw_box(t, start_x + current_pos*55, 50, 45, str(original_idx), "#ffa500")
        turtle.update()
        
    plaintext = "".join(plaintext_list)
    update_status(writer_t, f"Decryption finished! Original word: {plaintext}")


def draw_menu(t):
    t.clear()
    t.penup()
    t.goto(0, 150)
    t.pencolor("black")
    t.write("CIPHER ANIMATOR", align="center", font=("Arial", 28, "bold"))
    
    t.goto(0, 80)
    t.write("1. Bifid Cipher", align="center", font=("Arial", 20, "normal"))
    
    t.goto(0, 30)
    t.write("2. Permutation Cipher", align="center", font=("Arial", 20, "normal"))
    
    t.goto(0, -20)
    t.write("3. Exit", align="center", font=("Arial", 20, "normal"))
    turtle.update()

def get_word(screen):
    word_input = screen.textinput("Input Required", "Enter a word (maximum 8 letters):")
    if not word_input:
        return None
    word_input = "".join(filter(str.isalpha, word_input.upper())).replace("J", "I")[:8]
    if len(word_input) == 0: 
        return "SECRET"
    return word_input

def run_bifid(t, writer_t, word_input):
    bifid_ciphertext, sequence = animate_encryption(t, writer_t, word_input)
    
    writer_t.penup()
    writer_t.goto(0, -380)
    writer_t.pencolor("gray")
    writer_t.write("Wait 5 seconds for the Decryption phase...", align="center", font=("Arial", 12, "italic"))
    turtle.update()
    time.sleep(5)
    
    animate_decryption(t, writer_t, bifid_ciphertext, len(word_input))

def run_permutation(t, writer_t, word_input):
    cipher_key = list(range(len(word_input)))
    random.shuffle(cipher_key)
    
    perm_ciphertext = animate_permutation_encryption(t, writer_t, word_input, cipher_key)
    
    writer_t.penup()
    writer_t.goto(0, -380)
    writer_t.pencolor("gray")
    writer_t.write("Wait 5 seconds for the Decryption phase...", align="center", font=("Arial", 12, "italic"))
    turtle.update()
    time.sleep(5)
    
    animate_permutation_decryption(t, writer_t, perm_ciphertext, cipher_key)

def wait_for_menu_return(writer_t):
    writer_t.penup()
    writer_t.goto(0, -380)
    writer_t.pencolor("gray")
    writer_t.write("Animation Complete! Returning to Main Menu in 5 seconds...", align="center", font=("Arial", 14, "bold"))
    turtle.update()
    time.sleep(5)

def main():
    screen = setup_screen()
    t = turtle.Turtle()
    t.hideturtle()
    
    writer_t = turtle.Turtle()
    writer_t.hideturtle()
    
    while True:
        t.clear()
        writer_t.clear()
        draw_menu(t)
        
        choice = screen.textinput("Main Menu", "Select an option:\n1. Bifid Cipher\n2. Permutation Cipher\n3. Exit")
        
        if choice == '1':
            word = get_word(screen)
            if word:
                run_bifid(t, writer_t, word)
                wait_for_menu_return(writer_t)
        elif choice == '2':
            word = get_word(screen)
            if word:
                run_permutation(t, writer_t, word)
                wait_for_menu_return(writer_t)
        elif choice == '3' or choice is None:
            break
            
    t.clear()
    writer_t.clear()
    t.penup()
    t.goto(0, 0)
    t.pencolor("black")
    t.write("Goodbye!", align="center", font=("Arial", 28, "bold"))
    turtle.update()
    time.sleep(1.5)
    
    try:
        screen.bye()
    except turtle.Terminator:
        pass

if __name__ == "__main__":
    main()