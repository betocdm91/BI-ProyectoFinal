train = [
     ("Lo mejor del futuro es que viene un dia a la vez.", 'positive'),
     ("hijos de la chingada", 'negativo'),
     ("La amistad entre dos mujeres comienza o acaba por ser un complot contra una tercera...", 'neutral'),
     ("Canta las canciones", 'positive'),
     ("Un saludo para todos esos Narnianos!!!", 'positive'),
     ("MALDITOS HDP!", 'negative'),
     ("Preocupate si te deja en visto", 'negative'),
     ("Pobres personas", 'negative'),
     ("Alcoholismo es una palabra muy fuerte", 'negative'),
     ("Esto es genial", 'positive'),
     ("Ojala que te vaya bien", 'positive'),
     ("Eres un antipatico", 'positive'),
     ("Eres pesimo para esto", 'negative'),
     ("No se si hacer esto o lo otro", 'neutral'),
     ("No puedo con esto", 'negative'),
     ("Creer en ti", 'positive'),
     ("No sale el proyecto", 'negative'),
     ("Que rico que sabe", 'positive'),
     ("No todo esta mal", 'neutral'),
     ("Solo es peso muerto", 'negative'),
     ("Lo hiciste bien", 'positive'),
     ("Hay que ser positivo", 'positive'),
     ("No esta bien que lo hayas hecho", 'negative'),
     ("Deberia ser de otra forma", 'neutral'),
     ("Los proyectos no deberian ser tan largos", 'neutral'),
     ("Me regalaron un punto para pasar", 'positive'),
     ("Ya lo hizo", 'neutral'),
     ("Fue un accidente", 'negative'),
     ("El examen estaba facil", 'positive'),
     ("El examen estaba imposible", 'positive'),
     ("Lo bueno si dura", 'positive'),
     ("Todo en exceso es malo", 'negative'),
     ("Te lo advierto", 'negative'),
     ("Ingeniera colabore", 'neutral'),
     ("Le dieron like", 'positive'),
     ("Mi avatar es genial", 'positive'),
     ("Todos te odian", 'negative'),
     ("Hay que hacerlo", 'neutral'),
     ("Quien habla mal de mi a mis espaldas mi culo lo contempla", 'neutral'),
     ("El inspira confianza", 'positive'),
     ("El racismo es malo", 'negative'),
     ("En la vida es mas importante saber aceptar una derrota que celebrar una victoria", 'neutral'),
     ("Que bueno que ya se acaba el semestre", 'positive'),
     ("Ya no le voy a ver", 'negative'),
     ("Un pasado no superado", 'negative'),
     ("El amor es ciego hasta que te casas", 'neutral'),
     ("No hace falta un ramo de rosas para hacer sonreir a una mujer", 'neutral'),
     ("A la verga con esto jajaja", 'neutral'),
     ("Es genial jaja", 'positive'),
     ("Vamos con todo", 'positive'),
     ("Al fin me gradue", 'positive'),
     ("Que bueno que no les vuelvo a ver", 'neutral'),
     ("Las putas son putas", 'negative'),

    ("Esto no esta bien", 'negative')
 ]
test = [
    ("Como creer en lenin si invitan a los amiwis del grupo Escoria de lolacienfuegos para premiar con invitaciones?",'neutral'),
    ("Ya mismo a JG se le presenta un matrimonio en Miami! Pilas FiscaliaEcuador", 'neutral'),
    ("Avion de Tame accidentado en Cuenca sera vendido y cortado en partes ,", 'negative'),
    ("Plex Launches Live TV Support for Apple TV App - Mac Rumors ,", 'positive'),
    ("Con todo mi love para ti jonanperrea ,", 'positive'),
    ("PESO MUERTO CON 170 KG... CARITA... CASANASGYM GIMNASIOCASANAS INSANETRAININGCASHMUSCLE.,", 'neutral'),
    ("Que bestia... Que terrible salir a comprar las listas de utiles de las guaguas... Cansancio fisico y mental...", 'negative'),
    ("lahistoriaec no hubo diferencia robaron como todos los gobiernos anteriores. Ojala Lenin pido la renuncia de Glass.",'neutral'),
    ("Esos audios super producidos. No son conversaciones espontaneas.", 'neutral'),
    ("Primera entrada entregada a Luis de la Cruz, familiar de todos los ex futbolistas del Chota", 'positive'),
    ("Acaba de publicar una foto Ministerio Energia Ecuador", 'neutral'),
    ("Con todo mi love para ti jonanperrea ", 'positive')
 ]


from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)

#cl.classify("This is an amazing library!")
prob_dist = cl.prob_classify("Esto es genial.")
prob_dist.max()
round(prob_dist.prob("pos"), 2)
round(prob_dist.prob("neg"), 2)
from textblob import TextBlob
blob = TextBlob("La cerveza es buena. El chuchaqui es lo malo.", classifier=cl)
blob.classify()
print (cl.accuracy(test))
