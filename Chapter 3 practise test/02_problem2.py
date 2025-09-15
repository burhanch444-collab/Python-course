letter = '''Dear |Name|
 you are selected for job
 <|Date|>'''
print(letter.replace("Dear |Name|","Hello Burhan").replace("<|Date|>","25 october,2026"))