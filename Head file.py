import Field

    
size, quan = map(int, input().split())
field = Field.Field(size, quan)
field.matrix_done()
field.folder = f"Size {field.size}\\Variant with {field.queens} queens"
field.creat_folder()


field.recursion(0)
location = f"J:\\Files\\Python\\Homeworks\\Queens\\Variations\\{field.folder}\\Positions.txt"
with open(location, "w") as letsdo:
    q = 1
    for variation in field.all_var:
        letsdo.write(f"Var number {q}\n")
        for line in variation:
            for col in line:
                letsdo.write(col)
            letsdo.write("\n")
        letsdo.write("\n")
        q += 1


print("done")  