from random import randrange

def decrypt(encrypted_text, shift_pos):
	decrypted_text = ""
	dcr_shift = encrypted_text[shift_pos]
	encrypted_text = encrypted_text[:shift_pos] + encrypted_text[shift_pos + 1:]
	for i in encrypted_text:
		decrypted_text += str(chr(ord(i) - int(dcr_shift)))
	print(decrypted_text)

def encrypt(text, enc_shift):
	encrypted_text = ""
	for i in text:
		encrypted_text += str(chr(ord(i) + enc_shift))
	shift_pos = randrange(0, len(encrypted_text))
	# print(shift_pos)
	encrypted_text = encrypted_text[:shift_pos] + str(enc_shift) + encrypted_text[shift_pos:]
	print(encrypted_text)
	decrypt(encrypted_text, shift_pos)

def message():
	text = input("Enter message:\n")
	def enc_shift_get():
		enc_shift = int(input("Enter the shift value (1-9): "))
		if enc_shift < 1 or enc_shift > 9:
			print("Enter value ONLY between 1 and 9 (Both inclusive)")
			enc_shift_get()
		else:
			return enc_shift
	encrypt(text, enc_shift_get())

message()
