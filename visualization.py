import turtle
import time

# --- SETTINGS ---
CELL_SIZE = 45
GRID_X = -110
GRID_Y = 220
SPEED_MULTIPLIER = 1.5  # Increase this to make it even slower, decrease to make it faster

def setup_screen():
    screen = turtle.Screen()
    screen.title("Animacioni i Shifrës Bifid - Clean & Slow")
    screen.setup(width=900, height=850)
    screen.bgcolor("#ffffff")
    screen.tracer(0) 
    return screen

def draw_box(t, x, y, size, text, fill_color="white", text_color="black"):
    """Draws a square with text inside."""
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
    """Draws the static 5x5 Polybius grid."""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # Draw Column Numbers (Top)
    for col in range(5):
        draw_box(t, GRID_X + col*CELL_SIZE, GRID_Y + CELL_SIZE, CELL_SIZE, str(col+1), "#eeeeee", "blue")
    
    # Draw Row Numbers (Left)
    for row in range(5):
        draw_box(t, GRID_X - CELL_SIZE, GRID_Y - row*CELL_SIZE, CELL_SIZE, str(row+1), "#eeeeee", "blue")
        
    # Draw the Grid Cells
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
    """Animates the process of finding a character using Row and Column."""
    row_y = GRID_Y - (r-1)*CELL_SIZE
    col_x = GRID_X + (c-1)*CELL_SIZE
    
    # 1. Highlight Row Number
    draw_box(t, GRID_X - CELL_SIZE, row_y, CELL_SIZE, str(r), "#ffa500", "white") # Orange
    turtle.update()
    time.sleep(0.8 * SPEED_MULTIPLIER)
    
    # 2. Highlight Column Number
    draw_box(t, col_x, GRID_Y + CELL_SIZE, CELL_SIZE, str(c), "#ffa500", "white") # Orange
    turtle.update()
    time.sleep(0.8 * SPEED_MULTIPLIER)
    
    # 3. Highlight Intersection Cell
    draw_box(t, col_x, row_y, CELL_SIZE, char, final_color, "black")
    turtle.update()
    time.sleep(1.5 * SPEED_MULTIPLIER)
    
    # 4. Restore everything to normal colors
    draw_box(t, GRID_X - CELL_SIZE, row_y, CELL_SIZE, str(r), "#eeeeee", "blue")
    draw_box(t, col_x, GRID_Y + CELL_SIZE, CELL_SIZE, str(c), "#eeeeee", "blue")
    draw_box(t, col_x, row_y, CELL_SIZE, char, "white", "black")
    turtle.update()

def highlight_cell_simple(t, r, c, char, color):
    """A simple highlight for when we are just finding the coordinates of a known letter."""
    x = GRID_X + (c-1)*CELL_SIZE
    y = GRID_Y - (r-1)*CELL_SIZE
    draw_box(t, x, y, CELL_SIZE, char, color)
    turtle.update()
    time.sleep(1.0 * SPEED_MULTIPLIER) 
    draw_box(t, x, y, CELL_SIZE, char, "white") 
    turtle.update()

def update_status(writer_t, text):
    """Clears old text and writes the new step cleanly."""
    writer_t.clear()
    writer_t.penup()
    writer_t.goto(0, -30)
    writer_t.pencolor("darkred")
    writer_t.write(text, align="center", font=("Arial", 16, "bold"))
    turtle.update()

def animate_encryption(t, writer_t, word):
    t.clear()
    draw_polybius_grid(t)
    start_x = - (len(word) * 45) / 2 # Center the boxes dynamically
    
    update_status(writer_t, f"1. Gjetja e Koordinatave për: {word}")
    time.sleep(1)
    
    rows, cols = [], []
    
    # Step 1: Find coordinates
    for i, char in enumerate(word):
        r, c = get_coords(char)
        
        # Draw Plaintext Letter
        draw_box(t, start_x + i*45, -70, 35, char, "#dddddd")
        turtle.update()
        time.sleep(0.5 * SPEED_MULTIPLIER)
        
        # Highlight in grid
        highlight_cell_simple(t, r, c, char, "#ffea00")
        
        # Draw Row and Column coordinates below
        draw_box(t, start_x + i*45, -120, 35, str(r), "lightblue")
        draw_box(t, start_x + i*45, -160, 35, str(c), "lightgreen")
        rows.append(r)
        cols.append(c)
        turtle.update()
        
    time.sleep(1 * SPEED_MULTIPLIER)
    
    # Step 2: Combine
    update_status(writer_t, "2. Bashkimi i Rreshtave me Kolonat në një varg")
    combined = rows + cols
    start_comb_x = - (len(combined) * 35) / 2
    
    for i, num in enumerate(combined):
        color = "lightblue" if i < len(rows) else "lightgreen"
        draw_box(t, start_comb_x + i*35, -230, 35, str(num), color)
        turtle.update()
        time.sleep(0.3 * SPEED_MULTIPLIER)
        
    time.sleep(1.5 * SPEED_MULTIPLIER)
    
    # Step 3: Find New Characters
    update_status(writer_t, "3. Leximi i çifteve të reja (Rresht, Kolonë) për tekstin e shifruar")
    ciphertext = ""
    for i in range(0, len(combined), 2):
        r, c = combined[i], combined[i+1]
        new_char = get_char(r, c)
        ciphertext += new_char
        
        # Highlight the two numbers being used
        draw_box(t, start_comb_x + i*35, -230, 35, str(r), "#ffea00")
        draw_box(t, start_comb_x + (i+1)*35, -230, 35, str(c), "#ffea00")
        turtle.update()
        
        # Animate the Row/Col intersection in the grid!
        show_intersection(t, r, c, new_char, "#00ff00")
        
        # Draw the resulting character
        draw_box(t, start_x + (i//2)*45, -310, 35, new_char, "#00ff00")
        
        # Reset the number colors back
        color1 = "lightblue" if i < len(rows) else "lightgreen"
        color2 = "lightblue" if i+1 < len(rows) else "lightgreen"
        draw_box(t, start_comb_x + i*35, -230, 35, str(r), color1)
        draw_box(t, start_comb_x + (i+1)*35, -230, 35, str(c), color2)
        turtle.update()
        
    update_status(writer_t, f"Kriptimi përfundoi! Teksti i shifruar: {ciphertext}")
    return ciphertext, combined

def animate_decryption(t, writer_t, ciphertext, original_len):
    t.clear()
    draw_polybius_grid(t)
    start_x = - (len(ciphertext) * 45) / 2
    
    update_status(writer_t, f"1. Gjetja e koordinatave për tekstin e shifruar: {ciphertext}")
    time.sleep(1)
    
    combined = []
    
    # Step 1: Coordinates of Ciphertext
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
    
    # Step 2: Split in half
    update_status(writer_t, "2. Ndarja e vargut në gjysmë (Gjysma 1=Rreshtat, Gjysma 2=Kolonat)")
    half = len(combined) // 2
    for i in range(half):
        draw_box(t, start_x + i*45, -200, 35, str(combined[i]), "lightblue")
        draw_box(t, start_x + i*45, -240, 35, str(combined[half+i]), "lightgreen")
        turtle.update()
        time.sleep(0.4 * SPEED_MULTIPLIER)
        
    time.sleep(1.5 * SPEED_MULTIPLIER)
    
    # Step 3: Find Original Characters
    update_status(writer_t, "3. Leximi i koordinatave poshtë e lart për të gjetur fjalën")
    for i in range(half):
        r = combined[i]
        c = combined[half+i]
        orig_char = get_char(r, c)
        
        # Highlight the numbers being used vertically
        draw_box(t, start_x + i*45, -200, 35, str(r), "#ffea00")
        draw_box(t, start_x + i*45, -240, 35, str(c), "#ffea00")
        
        # Animate the Row/Col intersection in the grid!
        show_intersection(t, r, c, orig_char, "#00ff00")
        
        # Draw the restored character
        draw_box(t, start_x + i*45, -310, 35, orig_char, "#00ff00")
        
        # Reset number colors
        draw_box(t, start_x + i*45, -200, 35, str(r), "lightblue")
        draw_box(t, start_x + i*45, -240, 35, str(c), "lightgreen")
        turtle.update()
        
    update_status(writer_t, "Dekriptimi përfundoi! Fjala origjinale u rikthye.")

def main():
    screen = setup_screen()
    t = turtle.Turtle()
    t.hideturtle()
    
    # Use a separate turtle just for writing text so we can clear it cleanly
    writer_t = turtle.Turtle()
    writer_t.hideturtle()
    
    fjala = screen.textinput("Hyrja", "Shkruani një fjalë (maksimumi 8 shkronja):")
    if not fjala:
        fjala = "SEKRET"
    fjala = "".join(filter(str.isalpha, fjala.upper())).replace("J", "I")[:8]
    if len(fjala) == 0: fjala = "SEKRET"

    # Faza e Kriptimit
    teksti_shifruar, vargu = animate_encryption(t, writer_t, fjala)
    
    # Wait before decryption
    writer_t.penup()
    writer_t.goto(0, -380)
    writer_t.pencolor("gray")
    writer_t.write("Prisni 6 sekonda për fazën e Dekriptimit...", align="center", font=("Arial", 12, "italic"))
    turtle.update()
    time.sleep(6)
    
    # Faza e Dekriptimit
    animate_decryption(t, writer_t, teksti_shifruar, len(fjala))
    
    writer_t.penup()
    writer_t.goto(0, -380)
    writer_t.pencolor("gray")
    writer_t.write("Klikoni kudo në dritare për ta mbyllur.", align="center", font=("Arial", 12, "italic"))
    turtle.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()