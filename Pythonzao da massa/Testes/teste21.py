times = ['Pal', 'Fla', 'Int', 'Gre', 'Sao', 'Atl-mg', 'Cru', 'Atl-pa', 'San', 'Bah', 'Bot', 'Flu', 'Cor', 'Vas', 'Spo', 'Cea', 'Cha', 'Vit', 'Ame', 'Par']
for aux in range(65, 90):
    for i in range(20):
        if chr(aux) in times[i]:
            print(times[i])
        
