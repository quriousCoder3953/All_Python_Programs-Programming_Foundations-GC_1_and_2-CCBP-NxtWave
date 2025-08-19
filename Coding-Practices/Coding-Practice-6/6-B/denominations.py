N = int(input())
five_rupees_notes = N // 5
one_rupee_notes = N % 5
five_notes_final_count = "5:" + str(five_rupees_notes)
one_notes_final_count = "1:" + str(one_rupee_notes)

print(five_notes_final_count)
print(one_notes_final_count)
