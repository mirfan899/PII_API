from commonregex import CommonRegex
parsed_text = CommonRegex("""John, please get that article on www.linkedin.com to me by 5:00PM 
                               on Jan 9th 2012. 4:00 would be ideal, actually. If you have any 
                               questions, You can reach me at (519)-236-2723x341 or get in touch with
                               my associate at harold.smith@gmail.com""")
print(parsed_text.dates)
print(parsed_text.links)
print(parsed_text.phones)
print(parsed_text.emails)
print(parsed_text.credit_cards)