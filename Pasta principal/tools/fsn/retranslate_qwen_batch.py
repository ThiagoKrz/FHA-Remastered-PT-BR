from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fix_epk_script_blocks import rebuild_file_bytes_preserving_structure, split_text_lines


ROW_PREFIX_RE = re.compile(r"^(?P<id>\d+)::(?P<label>\$\$\$[^$]+\$\$\$)::")
ROW_RE = re.compile(r"^(?P<id>\d+)::(?P<label>\$\$\$[^$]+\$\$\$)::(?P<text>.*?)(?:::)?$")


PATCH_ROWS = r'''
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4256	Olho distraidamente para o quintal e vejo um monte de folhas caídas.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4257	Ainda tenho um tempinho, então resolvo dar uma limpada no quintal.[seloop storage=se513.wav][lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4258	Como hoje não venta, junto todas as folhas secas num instante.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4260	Viro para quem falou. Saber me observa. Parece que ela acabou de sair pela porta da frente da casa.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4261	"Oh, Saber. Estou limpando o quintal, como você pode ver."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4262	[chgfg time=300 storage=セイバー私服04e(遠) textoff=0]Mostro a ela a vassoura que tenho na mão.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4263	Saber olha para o monte de folhas, depois para o tamanho do quintal, e suspira.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4264	"Deve ser difícil fazer isso sozinho. Por que não pediu ajuda a ninguém?"[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4265	"Hã...? Não teve motivo nenhum. Eu só achei que faria sozinho."
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4266	"Shirou, duas pessoas trabalham mais rápido do que uma. Isso reduziria o seu trabalho. Nós também moramos nesta casa, então você deveria ter pedido."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4267	Exasperada, Saber toma a vassoura da minha mão.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4268	"Bom, tudo bem, mas[line len=2]"
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4269	"Escute. Não há nada de errado em pedir ajuda. Se algum de nós estiver sem fazer nada, o natural é pedir nossa ajuda."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4270	Ela encosta a ponta do cabo da vassoura no meu nariz.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4271	"Tá bom. Vou fazer o meu melhor."
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4272	"...Hrm. Muito bem. Agora você já sabe o que fazer da próxima vez."[wait canskip=false time=300][wvs][seloop storage=se513.wav][clfg time=300 rule=シャッター左から storage=セイバー私服02c(中) textoff=0][lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4274	...Ela é mesmo esforçada.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4275	Eu só pretendia fazer uma limpezinha, [sestop time=1000 nowait=true]mas, já que estamos nisso, puxamos o carrinho e o enchemos com todas as folhas secas.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4276	Quando terminamos uma volta pelo quintal, o carrinho já está lotado.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4278	"Normalmente eu colocaria isso para a coleta junto com o resto do lixo queimável."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4279	[chgfg time=300 storage=セイバー私服04e(中) textoff=0]Mas hoje temos folhas demais, então há algo que quero tentar.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4280	"Vai fazer algo diferente desta vez?"[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4281	"É. Estou pensando em fazer uma fogueira, já que temos tempo."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4283	"É. Já que surgiu a chance, melhor aproveitar.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4284	E hoje eu trouxe isto."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4285	Mostro a ela a sacola que trouxe da cozinha.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4287	"Batatas-doces. Aqui no Japão, existe o costume de assá-las na fogueira."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4289	Talvez seja exagero chamar isso de tradição, mas é algo que a gente faz.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4290	[chgfg time=300 storage=セイバー私服01a(中) textoff=0]Depois de embrulhar as batatas em papel-alumínio, acendo uma fogueira com as folhas secas.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4291	Como não choveu nos últimos dias, as folhas estão bem secas, e o fogo pega rapidinho.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4292	"Você parece ter prática com isso. Faz sempre?"[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4293	"Não muito. Talvez uma ou duas vezes por ano."
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4294	[chgfg time=300 storage=セイバー私服01b(中) textoff=0]Ouço o crepitar do fogo. Ao meu lado, Saber parece ainda mais relaxada do que de costume.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4295	"...Isso me traz lembranças."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4297	"Sim. O fogo sempre foi indispensável para aquecer, cozinhar e iluminar.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4298	Hoje em dia quase não o vejo mais, então olhar para ele me faz lembrar do passado."
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4299	[chgfg time=300 storage=セイバー私服06a腕b(中) textoff=0]...Entendi. Fontes de energia como eletricidade e gás natural só se tornaram comuns no último século ou coisa assim. Entre os Servos que conheço, só um teria convivido com isso em vida.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4300	"É uma visão tranquilizante."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4301	[chgfg time=300 storage=セイバー私服01b(中) textoff=0]Fico me perguntando o que Saber enxerga além das chamas.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4302	O fogo não me traz boas lembranças, então não consigo compartilhar dessa nostalgia.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4303	A fogueira se apaga quando a maior parte das folhas secas já foi consumida.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4304	Tomando cuidado para não espalhar as cinzas pretas, tiro as batatas-doces assadas com a atiçadeira.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4305	"Pronto. Acho que já basta."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4306	De luvas, tiro a fuligem delas e as embrulho em jornal.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4307	Ainda nem as abri, mas o cheiro já está ótimo.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4309	[chgfg time=300 storage=セイバー私服05d(中) textoff=0]Entrego a primeira batata-doce para Saber e começo a tirar o resto das cinzas.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4311	"Vou comer depois de tirar todas daqui. Vai em frente, prova uma primeiro. Ficam uma delícia bem quentinhas."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4313	O rosto de Saber se ilumina de surpresa depois da primeira mordida. [chgfg time=300 storage=セイバーfd特殊03_焼き芋a頬(中) textoff=0]Ela assente, satisfeita.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4314	"Está gostoso?"
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4316	[chgfg time=300 storage=セイバーfd特殊02_焼き芋d頬(中) textoff=0]Ela parece feliz da vida.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4317	Ainda bem. Já que ela se deu ao trabalho de me ajudar, esta pode ser a minha forma de agradecê-la.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4318	"...A propósito, Shirou, como você preparou essas batatas antes de assá-las?"[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4319	"Preparar? Eu só assei do jeito que estavam."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4320	Tiro duas ou três batatas e as embrulho em papel.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4321	[fg index=1000 time=300 pos=c storage=セイバーfd特殊02_焼き芋c(中)]Quando levanto os olhos, Saber parece ainda mais espantada do que antes.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4322	"...O que foi?"
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4323	"Nada. É que eu nunca imaginei que essas 'batatas-doces' pudessem ficar tão saborosas apenas sendo assadas."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4324	"Bem, dizem que os métodos mais simples de preparo são os melhores para realçar o sabor natural dos ingredientes."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4325	[clfg textoff=0 pos=all time=300]Na verdade, elas ficam ótimas só com fogo e um pouco de sal.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4326	"Mas, se é assim... por que esta batata assada tem um sabor tão diferente daquele modo rude de cozinhar?"[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4327	Saber deve estar comparando com algo que comeu em vida.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4328	"Se o gosto é diferente, mesmo sendo assada do mesmo jeito, talvez a diferença esteja nos ingredientes?"
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4329	"...A diferença é absurda.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4330	Se tivéssemos este sabor na minha época, nossos exércitos teriam lutado com ainda mais afinco..."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4331	Ela parece frustrada. Será que a batata-doce mexe com ela ainda mais do que o fogo?[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4332	Seja como for, ela não para de comer a batata-doce. Isso é bem a cara da Saber.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4333	"Frustração gastronômica parece assustadora."[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4337	...Um fio fino de fumaça sobe ao céu de outono.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4338	Sob essa fumaça, dividimos um lanche naquele acampamento perfeitamente tranquilo.[lr]
02urc2e6ku2kt4io7f9tj14f48.epk_dec	4339	Aquela cena pacífica, sem nada de extraordinário, ficou gravada na minha memória, mais brilhante do que qualquer sol de verão.
02urc2e6ku2kt4io7f9tj14f48.epk_dec	904313	O rosto de Saber se ilumina de surpresa depois da primeira mordida. Ela assente, satisfeita.[r]
4jggecm2s6cbb735ttb45fak9u.epk_dec	45455	"Nunca imaginei que um confronto com um expoente da Torre do Relógio terminaria assim... O destino é caprichoso, de fato."
4h3qkekrle62nckfhkn4eu02mc.epk_dec	28982	Será que a Fuji-nee está fazendo escola nela?
4h3qkekrle62nckfhkn4eu02mc.epk_dec	28986	Saber, nossa encostada oficial, desvia o olhar, desconfortável.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	28987	Tudo bem, sério. Se você começar a ficar encanada com isso, eu também vou ficar sem graça.
4h3qkekrle62nckfhkn4eu02mc.epk_dec	28988	"'Retribuir o favor'... Vai cozinhar para a gente?"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	28989	"Apesar da aparência, eu até que mando bem fazendo omeletes."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	28996	Só de olhar já dá para ver que isso é caro. Tem aquela aura daquelas bebidas com rótulo XO ou VSOP.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	28998	"Parece algum tipo de destilado."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29000	"É um elixir especial dos Einzbern. É uma delícia!"
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29004	"Heh, aposto que você não faz algo assim na mansão Tohsaka.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29005	Eu já disse ao Shirou antes: meu castelo tem uma destilaria."
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29008	Hmm? Elixires mágicos são feitos em destilarias?
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29009	"De fato, um castelo não pode prescindir de uma cervejaria ou de uma destilaria. Meus castelos também tinham adegas para bebidas finas. [cacheimage storage=セイバー私服07a(遠)][wvl][chgfg storage=セイバー私服07a(遠) time=300 textoff=0]Ainda assim, diziam-me que não se comparavam às vinícolas da Gália."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29014	"É um elixir, não um licor. Um único gole restaura uma quantidade notável de energia mágica, além do vigor físico. Na verdade, eu queria dar isso para você, Onii-chan, [cacheimage storage=イリヤ06c(中)][wvl][chgfg storage=イリヤ06c(中) time=300 textoff=0]mas hoje vou permitir, magnanimamente, que a Rin prove um pouco também."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29015	"Posso provar também, Illyasviel?"
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29019	Ela disse que um único gole do elixir já faz efeito. É uma espécie de tônico, ao que parece, então deve fazer bem à saúde. Provavelmente.
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29023	Me sinto até mal por não ter nenhum copo chique que combine com a classe dessa garrafa.
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29028	"Você é corajosa, Rin. Illyasviel, há algum problema se um Servo tomar isso?"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29029	"Sei lá... Hmm, acho que não deve causar nenhum efeito estranho."
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29031	"Ugh... Ei, isso está mesmo tudo bem?"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29032	Depois de ficar exposto ao aroma por alguns segundos, solto um gemido involuntário.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29034	"Nossa... isso parece ter uma pancada e tanto."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29037	"Toma!"
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29042	"Acho que isso vai pegar pesado para você, Shirou. Com tônicos assim, é importante não forçar seus limites."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29043	"Rin, põe gelo. [wvl][se storage=se560.wav]Saber, dilui com água. [cacheimage storage=イリヤ04b(中)][wvl][chgfg time=300 storage=イリヤ04b(中) textoff=0]Heheheheheeeh."[wait canskip=0 time=800][se storage=se561.wav]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29047	"...Você teve o trabalho de trazer isso para nós, [cacheimage storage=凛私服01e(中)][wvl][chgfg time=300 storage=凛私服01e(中) textoff=0]então pelo menos um gole eu vou tomar."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29048	"Pronto. Aqui."
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29049	Despejo um pouco do elixir no copo que me estendem.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29050	O copo da própria Illya só tem água. Hã? Ela não vai beber nada?
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29062	[chgfg time=300 storage=イリヤ11a(中) textoff=0]Cada uma delas comenta o que achou da bebida.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29063	Parece que elas gostaram. Eu, por outro lado, não tenho a menor vontade de me servir mais.[clfg textoff=0 time=300 pos=all rule=シャッター上から]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29064	Uégh, minha língua ainda está formigando.[stophaze time=400][lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29065	Ponho um pouco de água do jarro na boca e bochecho...[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29066	"Que diabos de miado foi esse...?"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29069	Olho para ver o que aconteceu, [rep fliplr=0 storages=凛私服12b(中),セイバー私服01e(中),イリヤ07a(中) time=300 flipudr=0 poss=r,l,c bg=i衛宮邸居間(fd)-(夜) indexes=1000,2000,3000 textoff=0]e encontro as duas me encarando, com os copos vazios.
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29074	Será que o elixir era tão potente assim? Será que abasteceu demais a energia mágica dela?
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29075	"...Isso era para ser um miado, Rin?"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29076	"Miau? [cacheimage storage=凛私服10e頬(近)][wvl canskip=false time=400][chgfg time=300 storage=凛私服10e頬(近) textoff=0]Do que você está miando, Meowsviel? Eu nem miei nada..."
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29079	"Ahah, ahn, miau. Eu tô me sentindo miauuito bem, [cacheimage storage=凛私服13b頬(近)][wvl][chgfg time=300 storage=凛私服13b頬(近) textoff=0]então por que você não bebe miais, Shirou?"
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29083	"[movefg opacity=255 left=-523 top=70 time=300 accel=2 storage=セイバー私服01e(近) textoff=0][movefg opacity=255 time=400 pos=c accel=-2 storage=イリヤ07b(近) textoff=0]Ei, Illya, você tem certeza de que esse elixir é seguro?"[wm canskip=0][wm canskip=0][lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29084	"Hã? Que estranho... Não me diga..."
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29085	[chgfg time=300 storage=イリヤ10c(近) textoff=0]Confusa, Illya destampa a garrafa e cheira o conteúdo...[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29088	"Ah, a Leys deve ter colocado algumas amostras de teste nesta garrafa, porque todas parecem iguais. Era inevitável que eu confundisse."
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29089	[chgfg time=300 storage=イリヤ06e(近) textoff=0]Illya diz "tee-hee" e dá uma batidinha zombeteira na própria cabeça.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29091	"Eu não imaginava que isso fosse acontecer quando tirei isso escondido debaixo do nariz da Sella..."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29092	"\"Amostras de teste\", foi isso que você disse?"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29093	"É. Elas fazem umas coisas engraçadas acontecerem, mas basicamente são inofensivas. Agora a reação da Rin faz sentido."
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29094	"Então para de rodeios, Meowsviel, [cacheimage storage=イリヤ07d(近)][wvl][chgfg time=300 storage=イリヤ07d(近) textoff=0]e conta logo o que você sabe!"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29096	É uma droga que embaralha seus sentidos e a fala?[wm canskip=0][wm canskip=0]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29100	[move time=150 path=(123,30,255)(149,23,255)(124,30,255)(153,23,255) storage=凛私服05g(近) accel=0 spline=1 textoff=0][move time=170 path=(-8,215,255)(4,208,255)(-7,216,255)(5,207,255) storage=イリヤ08b(近) accel=0 spline=1 textoff=0]Tohsaka sorri para Illya com uma alegria nada disfarçada.[wm canskip=0][wm canskip=0]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29101	[chgfg time=200 storage=凛私服06b(近) textoff=0]Ainda bem que tive um mau pressentimento e não bebi mais do que já tinha bebido. Sim, [chgfg time=200 storage=凛私服10e頬(近) textoff=0]tem alguma coisa errada com quem consegue virar um copo inteiro depois de sentir esse cheiro.[chgfg time=200 storage=凛私服09d(近) textoff=0][lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29106	[move time=260 path=(153,20,255)(153,39,255)(153,23,255)(153,33,255)(153,20,255)(153,39,255) storage=凛私服14d頬(近) accel=-2 spline=1 textoff=0]Enquanto pergunto isso, puxo Illya para trás de mim para protegê-la.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29108	"Fiz. Até dei um pouco para a Taiga provar, só por garantia."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29109	"Ah. E ela virou um tigre?"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29118	"E-eu... estou bem, rawrrrr..."[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29124	Aham. Entendi. A Saber virou um leão.[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29127	"Miau! Como é que nunca miaucontece nada com você, mas sempre miaucontece com a gente!?"[lr]
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29128	"Então vai ficar brava com a Illya primeiro! Ela provavelmente viraria uma raposa ou algo assim!"
4h3qkekrle62nckfhkn4eu02mc.epk_dec	29132	"Não se faça de inocente. E vocês duas, se acalmem. Não teria graça nenhuma se eu começasse a latir."[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29344	Se ela se lembrava bem, o objetivo dela era investigar essa anomalia.
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29347	Até que rendeu alguma coisa.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29348	No entanto, apesar de vigiar um certo Servo do xintoísmo, ela não tinha obtido pista nenhuma.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29349	Há uma grande diferença entre ela e os outros Servos.
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29350	Os monstros que vagam pela noite...[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29351	Ninguém deveria conseguir notá-los até o último dia, mas ela percebe isso desde o começo.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29357	Um trabalho eternamente infrutífero.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29364	Na verdade, "poderia" é a palavra apropriada aqui.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29370	Monstros ou não, para ela não passam de lixo.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29379	Ela se banha mecanicamente no sangue.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29381	A respiração dela está começando a se descontrolar de novo.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29384	São só monstros, não têm fim, e essa é a tarefa que lhe foi dada.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29399	Os cadáveres deles, [wait canskip=0 time=500][dash hidefg=0 textoff=0 mx=0 opacity=255 layer=base irot=-0.03 cx=523 imag=1.7 time=100 cy=183 mag=1.7 my=0 storage=o形の無い島(暗黒)-(真紅) rot=-0.03 accel=0][noise monocro=1 type=ltDodge opacity=170]os cadáveres deles, [wait canskip=0 time=500][stopnoise][dash hidefg=0 textoff=0 mx=0 opacity=255 layer=base irot=-0.11 cx=347 imag=1.7 time=100 cy=309 mag=1.7 my=0 storage=o形の無い島(暗黒)-(真紅) rot=-0.11 accel=0]ela recolheu os cadáveres deles e...[rf]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29403	...[wait canskip=0 time=500][se storage=se028 nowait=1][fadein textoff=0 time=200 storage=red][clfg][dash textoff=0 page=back mx=0 opacity=255 layer=base irot=-0.0 cx=348 imag=1.3 time=100 cy=682 mag=1.3 my=0 storage=o形の無い島(暗黒)-(真紅) rot=-0.0 accel=0][fg left=-100 index=3000 top=400 storage=シネスコw1000b][fg left=-100 index=2000 top=-300 storage=シネスコw1000a][fg opacity=0 left=0 index=1000 top=0 storage=red2][transex textoff=0 time=400]...Ela não quer se lembrar.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29405	Os olhos da irmã dela sempre foram vivos e alegres, mas se tornaram brancos de medo...
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29406	...Ela continua o banquete em nome da "investigação."[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29409	Os monstros são mais fortes que os humanos, mas ainda estão muito longe de conseguir acompanhá-la. São o tipo de presa ideal para ela esmagar.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29412	Se existe um problema, é que não há limite para o quanto ela pode acelerar.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29418	Os monstros mataram todo mundo, ou eles nunca existiram para começo de conversa?[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29419	Deve ser a segunda opção.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29428	...ela não hesitou em empalá-la.
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29432	Uma humana só acabou entrando ali por acaso.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29434	Então não tem problema.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29436	"...Não está tudo bem.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29437	Não importa que tipo de criatura você seja nem qual seja a situação, [l][say storage=emimp30_kar_0002 name=カレン]você matou um ser humano."[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29455	Desesperada, ela insiste que foi um acidente,[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29456	alegando que tem um papel diferente.
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29459	As palavras dela escancaram o peito, expondo o coração ao ar de fora.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29461	Isso tudo foi pela sua Mestre...
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29462	"Nossa, que Servo leal.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29463	Mas será que isso é [font italic=true]mesmo[font italic=false] por ela? Fico pensando..."[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29470	Vou deixar você descansar agora. Para ser sincero, estou começando a me cansar de assistir a isso."[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29480	(Sem motivo nenhum...)[rf][lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29485	As vidas perdidas não vão desaparecer [wvl][se storage=se290.wav]só porque você evita olhar para elas.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29489	A agressora já nem se importa mais com o que essa humana é. Ela não passa de um incômodo.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29490	Então vai matá-la até ela se calar.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29491	Ela rasga o ventre morno dela e arranca suas entranhas.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29493	Ela nunca se sentiu tão bem descarregando a raiva nessa garota quanto se sentiu com todos os outros humanos que já matou!
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29497	"...Agora você entende, certo?[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29510	"Eu não me importo com o que aconteça com você, Medusa... mas preciso de um Servo."
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29674	"Ora, você consegue me ver?[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29733	...Servos são invocados por Mestres parecidos com eles.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29750	Claro, você é patético, [l][say storage=emimp30_anr_0072 name=アンリ]mas, enquanto ainda quiser salvar outra pessoa, ainda mal dá para dizer que deixou de ser humano."[rf][lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29761	Quando acordar, peça desculpas à sua Mestre.[lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29762	Eu sei que isso vale pouco vindo de mim, mas Mestre e Servo deveriam se dar bem."[rf][lr]
5knkbk3mojgc50o4nq5jcsspab.epk_dec	29763	A coisa dá uma risadinha antes de desaparecer.[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1045	O culpado foi a Fuji-nee, como eu suspeitava. Um mistério resolvido em tempo recorde.[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1050	Por ora, registro mentalmente que a Saber aceita qualquer coisa.
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1056	O que significa que a decisão cai nas minhas mãos...
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1069	"Você chama isso de compostura?"
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1079	Eu estava te deixando preocupado?"[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1082	"Eu só quis dizer que, para mim, é mais fácil porque você deixa claro quando gosta da comida.[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1083	E, Rider, a Saber tem bons modos à mesa."[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1088	É por isso que eu não acho que a sua preocupação seja justificada."[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1091	Há algo que você se recuse a comer, Rider?"[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1093	"Pensando bem... Provavelmente,[cacheimage storage=セイバー私服04e(中)][wvl][chgfg time=300 storage=セイバー私服04e(中) textoff=0] nada do que você costuma cozinhar."[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1097	Pensando nisso, a classe dela e o Fantasma Nobre me dão outra ideia.
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1102	"Vinho de cobra... a Fuji-nee trouxe uma coisa dessas?"
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1105	"Ela estava toda feliz se exibindo com isso na frente da Sakura e de mim.[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1106	Disse que não tinha graça se não assustasse alguém com aquilo, então largou aqui."[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1110	"Sim. Não tenho objeção a comer isso.[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1111	...Claro, não pretendo comer isso na frente de alguém que não gostaria de ver."[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1114	As duas, no entanto, demonstram certa consideração amistosa uma pela outra.
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1115	"Certo, certo, já entendi.[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1121	"Você quer que eu escolha os ingredientes do almoço?"[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1134	A tampa traz o rótulo "RAW: KEEP REFRIGERATED". Imagino que seja peixe ou algo assim.
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1138	Eu tento tirá-lo da embalagem, [wm canskip=0][movefg opacity=255 left=10 top=75 time=300 accel=-2 storage=セイバー私服06b腕b(中) textoff=0]mas as ventosas estão grudadas por dentro, e não consigo desgrudá-lo direito.[wm canskip=0]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1139	"[movefg opacity=255 left=-70 top=75 time=400 accel=2 storage=セイバー私服06b腕b(中) textoff=0][resumevoice]Esse troço é bem arisco."[cacheimage storage=ライダー私服02a(中)][wm canskip=0][movefg opacity=255 left=-50 top=75 time=300 accel=-2 storage=セイバー私服06b腕b(中) textoff=0][wvs][wm canskip=0][lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1140	"[movefg opacity=255 left=-130 top=75 time=400 accel=2 storage=セイバー私服06b腕b(中) textoff=0][resumevoice]Por que não comemos isso no almoço? [cacheimage storage=ライダー私服02a(中)][wvl][wm canskip=0][movefg opacity=255 left=-110 top=75 time=300 accel=-2 storage=セイバー私服06b腕b(中) textoff=0]Acho melhor aproveitar enquanto ainda está fresco.[wm canskip=0]"[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1141	[movefg opacity=255 left=-192 top=75 time=400 accel=2 storage=セイバー私服06b腕b(中) textoff=0]É verdade, ele vai ficar melhor se [wm canskip=0][movefg opacity=255 left=-172 top=75 time=300 accel=-2 storage=セイバー私服06b腕b(中) textoff=0]usarmos hoje[wm canskip=0].
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1142	"Certo, então o que eu poderia fazer com isso...? Saber, por que você está parada tão longe?"[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1154	"N-não pode ser... Você está me dizendo que isso continha aquele monstro marinho viscoso e inchado de outro mundo!?"
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1155	"Viscoso e inchado...?"[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1158	Ela está tremendo e me encara com uma expressão horrorizada. Será que ela ficou mesmo brava comigo?[wm canskip=0]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1160	"E-eu não fazia ideia de que esse 'polvo' de que você fala era aquele monstro do mar![lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1161	...Não acredito que eu andei pondo na boca aqueles deuses sombrios de outro mundo que nem morrem quando eu os parto ao meio...!"[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1165	Como se [chgfg time=200 storage=セイバー私服01c(中) textoff=0]tivesse voltado à vida ao sair da geladeira, [retainhaze][movefg textoff=0 both=1 opacity=155 left=-244 top=-100 time=600 accel=0 storage=049_黒炎][chgfg time=200 storage=セイバー私服08c(中) textoff=0]o polvo começa a enrolar os tentáculos no meu braço.[wm canskip=0]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1169	Do meu ponto de vista, é igualmente difícil acreditar que você consiga gostar de natto e de ameixas salgadas."[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1175	Enquanto me impressiono com a experiência de vida da Saber, [se storage=se420.wav][se storage=se419.wav][shock vmax=15 time=300 count=2]desgrudo o polvo da minha mão e o coloco na tábua de corte.[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1177	"E esse seu hábito de encharcar a comida com azeite? Isso sufoca todas as qualidades do prato."[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1180	Para começar, somos Servos. [cacheimage storage=ライダー私服01d(中)][wvl][chgfg time=300 storage=ライダー私服01d(中) textoff=0][movefg opacity=170 left=0 top=0 time=800 accel=0 storage=black textoff=0]Não faz sentido ser tão exigente com comida quando nem precisamos comer.[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1182	"Oh? Você está dizendo que se vestir como uma atendente de loja, por querer ter uma bicicleta ou uma motocicleta, não é algo superficial da parte de um Servo?"
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1184	Droga, fiquei tão concentrado em cozinhar que nem percebi no que isso estava se transformando![lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1185	Isso é ruim. Se eu não fizer alguma coisa logo, consigo ver tanto a minha querida casa quanto esta área inteira virando escombros...!
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1187	"Sakura...! Que timing perfeito![lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1188	P-por enquanto eu estou bem, mas consegue acalmar a Saber e a Rider?"[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1189	"Ah, tá...[seloop storage=se373.wav][wvl canskip=false time=400][sestop time=3000 nowait=1][clfg time=300 rule=シャッター左から pos=all textoff=0] Ei, Rider, o que você está fazendo com a Saber agora?[lr]
6dqcshrvriv9p4pnbjr3bfjes0.epk_dec	1198	Agradeço à Sakura enquanto ela começa a repreendê-las e vou cortando os ingredientes.[lr]
74ka9p8jraqds59k98apkki4ik.epk_dec\t42544\t"Shirou. Isso pode ser uma pergunta boba, mas o que exatamente são ovos de onsen?"
74ka9p8jraqds59k98apkki4ik.epk_dec\t42545\t"São ovos cozidos literalmente num onsen[line len=2]numa fonte termal. Não na água do banho que as pessoas usam, claro."
74ka9p8jraqds59k98apkki4ik.epk_dec\t42546\t"...É gostoso?"
74ka9p8jraqds59k98apkki4ik.epk_dec\t42547\t"Ah... [wait time=600][l][hffacechg chara=士郎 face=楽2 time=200][say storage=HSHI1_SHI_0030 _name=士郎]Bom, eles têm uma... aura diferente dos ovos cozidos comuns."
74ka9p8jraqds59k98apkki4ik.epk_dec\t42548\t"Entendo. É só cozinhar um ovo e, ainda assim...[l][hfsigh layer=0][say storage=HSHI1_SAV_0040 _name=セイバー] A culinária do seu país é bastante profunda."
74ka9p8jraqds59k98apkki4ik.epk_dec\t42549\t"...Tenho a impressão de que cozinhar era meio bruto na sua época."
74ka9p8jraqds59k98apkki4ik.epk_dec\t42550\t"Shirou. Se me permite ser franca, esse é um assunto proibido. Se estes fossem tempos menos pacíficos, um pedido de desculpas verbal não bastaria para reparar você ter tocado nele."
74ka9p8jraqds59k98apkki4ik.epk_dec\t42551\t"Hã...? Até perguntar sobre ovos cozidos?"
74ka9p8jraqds59k98apkki4ik.epk_dec\t42552\t"Sim. Nesse caso, eu exigiria um pedido de desculpas especialmente fervoroso."
74ka9p8jraqds59k98apkki4ik.epk_dec\t42553\t"Hmm. Bem, vai ser um pequeno passeio, mas quer provar ovos de onsen?"
74ka9p8jraqds59k98apkki4ik.epk_dec\t42554\t"...Podemos?"
74ka9p8jraqds59k98apkki4ik.epk_dec\t42555\t"Podemos. Dá para ver que você está curiosa."
74ka9p8jraqds59k98apkki4ik.epk_dec\t42556\t"S-[wvs][wait canskip=0 time=200][hfsigh layer=0][say storage=HSHI1_SAV_0100 _name=セイバー]sim, estou."
74ka9p8jraqds59k98apkki4ik.epk_dec\t42557\t"Ótimo. Então vamos."
74d8b4d600l83llv251rsk63lr.epk_dec\t45797\t"Hm, hmm, hmm[humming]"
74d8b4d600l83llv251rsk63lr.epk_dec\t45798\t"Acho que vamos conseguir transferir o ateliê, e agora demos mais um passo rumo à orquestra dos nossos sonhos."
74d8b4d600l83llv251rsk63lr.epk_dec\t45799\t"Além disso, esse banho de sangue em fonte termal é o auge do estilo! Ahh, agora sinto que minha vida inteira valeu a pena!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45800\t"...Hm? Eu acabei de chamar uma fonte [font italic=true]termal[font italic=false] de [font italic=true]refrescante[font italic=false]? Que estranho."
74d8b4d600l83llv251rsk63lr.epk_dec\t45801\t"Tanto faz. Ah, é mesmo. Como está sendo sua primeira experiência num onsen, grandalhão?"
74d8b4d600l83llv251rsk63lr.epk_dec\t45802\t"Ohh... Pensar que Jeanne pôde ser recriada tão pequena e com tamanha precisão!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45803\t"Esse rosto! Essa pele! Essa nuca! Sem sombra de dúvida, esta é a Jeanne que conheci naquele dia, naquele tempo e lugar!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45804\t"Agora eu entendo que a depravação do capitalismo não deve ser subestimada! ...Hm."
74d8b4d600l83llv251rsk63lr.epk_dec\t45805\t"Ei, grandalhão!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45806\t"Ah, desculpe, Ryunosuke. O que foi?"
74d8b4d600l83llv251rsk63lr.epk_dec\t45807\t"Eu perguntei se você está gostando do banho."
74d8b4d600l83llv251rsk63lr.epk_dec\t45808\t"Ah, do onsen? Hmm... O costume de ficar de molho num banho nunca se enraizou na minha cultura..."
74d8b4d600l83llv251rsk63lr.epk_dec\t45809\t"Mas acho isso bastante encantador."
74d8b4d600l83llv251rsk63lr.epk_dec\t45810\t"Eu sei, né? Você mergulha num banho quentinho para renovar o corpo e a mente. Dá a sensação de que amanhã vai poder dar o máximo de si."
74d8b4d600l83llv251rsk63lr.epk_dec\t45812\t"OOHHHHH!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45813\t"G-grandalhão!?"
74d8b4d600l83llv251rsk63lr.epk_dec\t45814\t"Jeanne! Um dos finos e adoráveis dedos da minha Jeanne acabou de se quebrar!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45815\t"Ahh... É porque você não para de mexer nela. Miniaturas quebram mais fácil do que gente. ...Oh."
74d8b4d600l83llv251rsk63lr.epk_dec\t45816\t"A-agora foi um fio de cabelo dela, algo que vale muito mais do que o próprio peso em ouro, que simplesmente... AHHHHH!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45817\t"Maldição! Até quando Deus vai brincar comigo antes de se dar por satisfeito!?"
74d8b4d600l83llv251rsk63lr.epk_dec\t45818\t"Deus nunca responde quando rezamos para Ele, mas ainda assim surge para atrapalhar nosso caminho sem ser chamado... Como Ele é podre e vil!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45819\t"Até uma criança sabe disso: faça aos outros o que gostaria que fizessem a você!"
74d8b4d600l83llv251rsk63lr.epk_dec\t45820\t"É, bem, se você vai continuar mexendo na miniatura, talvez devesse aparar essas unhas."
74d8b4d600l83llv251rsk63lr.epk_dec\t45821\t"Agora a tinta está saindo!!!"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41795\t"Por fim, chegaste.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41796\tPortadora do Santo Graal, miserável e bela, devotada ao teu desejo...[playstop time=400 nowait=1]"[nolr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41797\t"..."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41798\t"..."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41799\t"..."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41800\t"..."[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41801\t"...Isso está demorando. [wait canskip=0 time=300]Acho que é aquilo que dizem sobre pessoas parecidas demais não se darem bem. Nunca ia ser tão fácil... Espera, [wait canskip=0 time=400][hffacechg chara=ランサー face=怒 layer=0 time=200][hfstamp layer=0][se volume=80 storage=se564.wav]opa!"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41802\t"Tem um belo sujeito aqui, minha cara cuspida e escarrada... não, um pouco menos bonito do que eu, mas que claramente entende a minha dor!"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41803\t"Vejam só. Quando foi que isto virou um otome game celestial!?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41804\t"...[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41805\tNão, você é só um idiota."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41806\t"Não, não sou!"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41807\t"Estou brincando.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41808\tNão somos macacos olhando para um espelho. Nós dois sabemos do que se trata."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41809\t"Que raro. Dois Espíritos Heroicos idênticos serem invocados na mesma era."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41810\t"Isso é perfeitamente possível dentro do sistema dos Servos. Então estamos vendo um Cú Chulainn do bem e outro do mal?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41811\t"Mais ou menos. Só que eu sou neutro, então não é como se me dividisse em um lado bom e outro mau."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41812\t"Se há alguma diferença sutil em como me manifesto, ela deve vir da diferença entre os Mestres."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41813\t"Ah, cala a boca. Não nos ponha no mesmo saco quando você claramente só serve de alívio cômico."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41814\t"Como é que é, parceiro!?[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41815\tO que é tão engraçado em mim!?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41816\t"Hã?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41817\t"Hum, vamos dizer que isso é uma questão de criação em vez de natureza.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41818\t...Você tem a minha simpatia."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41819\t"Lancer, nunca imaginei que você pudesse ser o sensato da dupla. Ele deve ter sido abençoado com um colega e um chefe especialmente raros[line len=2]"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41820\t"O que vocês estão fazendo? Acabem logo com isso para podermos dar um[line len=2][wait canskip=0 time=400][hffacechg chara=ギルガメッシュ face=ポカーン layer=0 time=100]Q-[wait canskip=0 time=600][hffacechg chara=ギルガメッシュ face=喜 layer=0 time=100][play storage=bgm143.ogg][hfquake time=1000 vmax=8 hmax=8 layer=0 wait=0][hfquake layer=message0 time=1000 wait=0 vmax=8 hmax=8]UAU!"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41821\t"Essa combinação está tão escancaradamente fadada pelo destino que chega a me cegar![lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41822\tQuem é essa criança estonteantemente adorável, Lancer!?[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41823\tUm deus!?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41824\t"..."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41825\t"Eu já devia esperar que você se atirasse em qualquer um desde que fosse jovem e loiro.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41826\tMas ele é um menino, sabia."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41827\t"Nrgh. Não zombe de mim, tolo![lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41828\tNo meu registro real, qualquer coisa fofa está aprovada. Saiba que os [font italic=true]verdadeiros[font italic=false] heróis não discriminam por gênero!"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41829\t"Ora, essa. E pensar que, além de moralista, elitista, autocentrado e um monarquista incurável, você ainda é narcisista...[wait canskip=0 time=400][hffacechg chara=カレン face=喜2 layer=1 time=200] (fascinada)"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41830\t"Ahahahaha.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41831\tPessoal, vamos matar esse cara primeiro."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41832\t"Hm, outra verificação falhou.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41833\tOnde foi que eu errei, Lancer? Nem tive uma opção de diálogo."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41834\t"Provavelmente no instante em que você surgiu no mundo... Ei, Kotomine. Diga alguma coisa."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41835\t"...É, bem...[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41836\tEsta é uma reunião inesperada, mas o fato continua sendo que só o vencedor pode seguir adiante."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41837\t"Mas... garota.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41838\tVocê não parece ter um desejo próprio. O que faz aqui?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41839\t"...Suponho que se possa dizer que existe algo que eu quero, ainda que eu não tenha um desejo."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41840\t"Embora, pensando bem, talvez eu pudesse obtê-lo sem o poder do onsen."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41841\t"Oh? Se importaria de me dizer o que é?[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41842\tO que um ser inumano como você poderia desejar?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41843\t"Por ora, eu gostaria de firmar a minha posição."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41844\t"Mesmo agora, dá para ver como nossas personalidades, roupas e até nossos Servos se sobrepõem. É um belo aborrecimento, não acha?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41845\t"Então você usa o conflito para eliminar ameaças, em vez de construir a sua própria base.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41846\tE considera sua predecessora um incômodo?"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41847\t"Sim, e ainda por cima tenho uma longa lista de ressentimentos.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41848\tO que eu tanto quero...[se storage=se452.wav]é a sua vida."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41849\t"Que criança retorcida você é.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41850\tEntristece-me ver isso, como homem casado. Gostaria de ver a reação do seu pai."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41851\t"Quanto a isso, concordamos. Eu adoraria saber o que pensa o pai ausente que me 'criou' assim."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41852\t"...Embora eu tenha certeza de que sentiria uma vontade irresistível de vomitar ao ver o rosto dele."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41853\t"Heh."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41854\t"Hehe."[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41855\t[hfu][cm]"[hfl]"He[hfu]He[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]he[hfl]he[hfu]![hfl]![hfu]"[hfl]"[nolr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41856\t"Hahahahahahahahahahahahahahahaha!"[nolr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41857\t"Ótimo![lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41858\tIsso parece divertido! Tô dentro!"
748p1tmj8ehl3slidp7tcak138.epk_dec\t41859\t"Quem não sabe ler o ambiente é mesmo... cabeça-dura."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41860\t"Ahahahahaha.[lr]
748p1tmj8ehl3slidp7tcak138.epk_dec\t41861\tEu realmente quero ver esse homem morto."
748p1tmj8ehl3slidp7tcak138.epk_dec\t41862\t"Ah, mas não adianta matá-lo aqui... O futuro é cruel demais... Não quero crescer..."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17120\tNo caminho pela passarela, vejo uma cena que chama minha atenção.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17121\t"Espera, Saegusa, da turma da Tohsaka...?"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17122\tAquela garota saltitante vista de costas é a Saegusa.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17123\tNão chegamos a trocar olhares, então o normal seria só seguir meu caminho...
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17124\t"Surpresa. Você é do Homurahara, Yukika? Achei que fosse mais nova."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17125\t"Sou, sim. Desculpa, Gil. Na verdade, sou bem mais velha do que você."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17126\t"Ah... Não, quem deve se desculpar sou eu. Foi um lapso. Que vergonha, para um homem, perguntar a idade de uma mulher."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17127\t"Ah, mas isso me deixa um pouco feliz. Prefiro que você seja como uma irmã mais velha em vez de só uma amiga."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17128\t"Hehe, obrigada. Eu também adoraria ter um irmãozinho calmo como você, Gil. Os meus são todos uns pestinhas."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17129\t"Haha, o Kota e os outros realmente são cheios de energia.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17130\tVivem correndo por aí sem medo de nada. Você rala bastante, Yukika."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17131\t"É. Gil, se meus irmãozinhos estiverem prestes a aprontar alguma imprudência, você pode segurá-los por mim?[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17132\tEles não me escutam por mais que eu fale, mas escutam tudo o que você diz, não é? Eles te respeitam, Gil."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17133\t"Não é isso. Eles escutam o que você diz, Yukika.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17134\t[chgfg textoff=0 time=300 storage=由紀香私服02c(中)] Mesmo que eu não esteja por perto, não há com que se preocupar. Afinal, o Kota e os outros não fariam nada que a deixasse triste."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17135\t"...Bem, o problema é que eles estão sempre tentando te dar trabalho. Nem eu consigo demovê-los disso."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17136\t"...Eles parecem se dar bem... O que ele está fazendo com a Saegusa...?"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17137\tObservo os dois escondido atrás de um banco.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17138\tAquela criança dourada é, sem sombra de dúvida, Gilgamesh.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17139\tHoje ele é uma figura carismática entre as crianças de Miyama, conhecido como o "Padrinho da Máfia Infantil."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17140\t"Aliás, Yukika, você não tem treino de atletismo hoje, certo? Está livre à tarde?"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17141\t"Sim, estou livre. Lavei roupa de manhã, então ia só relaxar até a hora do jantar."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17142\t"Entendo. Então você veio passear no parque.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17143\tQue bom. Eu tinha acabado de me fartar da minha guardiã e vindo até o parque, mas parece que a minha sorte mudou."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17144\t"Hã? Ah, hum... Sua mãe é, bom..."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17145\t"Ah, foi o Kota e os outros que te contaram?[cacheimage storage=ギル子供01d(中)][wvl][chgfg textoff=0 time=200 storage=ギル子供01d(中)] ...Hum, ela não é minha mãe, mas é minha guardiã. É uma pessoa difícil, que se irrita por qualquer coisinha. O completo oposto de você.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17146\tNão, seria até grosseiro com você fazer essa comparação. Ela não passa de uma dona de casa, enquanto você é a pessoa de quem eu gosto.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17147\tSe eu precisasse mesmo de uma guardiã, eu gostaria que tivesse sido você... como minha Mestre."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17148\t"Hã... 'Mestre'...? [cacheimage storage=由紀香私服02i(中)][wvl][chgfg textoff=0 time=300 storage=由紀香私服02i(中)]Não, mais importante, hum..."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17149\t"Sim, a pessoa de quem eu gosto. [wvl][move textoff=0 time=120 path=(401,85,255)(416,78,255)(434,82,255) storage=由紀香私服02i(中) accel=0]Eu disse que prefiro alguém como uma irmã mais velha a uma simples amiga, não disse?[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17150\tE você, Yukika? Já ficou com alguém mais novo?"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17151\t"H-Hum, Gil, o que...!?"
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17152\t"Aquele desgraçado...! Finalmente mostrou a verdadeira face...!"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17153\tEntão aquele jeito certinho era só uma máscara![lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17154\tNesse ritmo, a Saegusa vai acabar sendo devorada...!
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17155\t"Pode parar aííí! O que pensa que está aprontando num parque tão pacífico, seu tarado!"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17156\t"E-Emiya!?"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17157\t"Ah, senhor."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17158\tSaegusa se afasta num pulo do menino loiro.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17159\tJá o pequeno Gil me encara daqui com evidente desagrado.
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17160\t"T-Tchau, Emiya! [cacheimage storage=由紀香私服01i(中)][wvl canskip=0 time=200][chgfg textoff=0 time=200 storage=由紀香私服01i(中)]Acabei de lembrar que tenho uma coisa para fazer... [cacheimage storage=由紀香私服01g頬(中)][wvl canskip=0 time=200][chgfg textoff=0 time=200 storage=由紀香私服01g頬(中)]Até mais...!"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17161\tO coelhinho selvagem escapa.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17162\tAo ver o quanto ela entrou em pânico, eu me arrependo do que fiz.
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17163\t"...Ora, quem você está chamando de tarado? Justo vindo de você, isso é a última coisa que eu queria ouvir."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17164\t"É a verdade, não é? Por que estava dando em cima da Saegusa?[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17165\tNão sei que tipo de jogo você está jogando, mas há gente com quem você pode brincar e gente com quem não pode."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17166\t"Ei, quem está sendo rude aqui é você. Eu realmente gosto da Yukika.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17167\t"Ah, fala sério! ...Espera, quer dizer, é rude duvidar de você nessas coisas.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17168\tAh... Hum, está falando sério mesmo?"
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17169\t"Não estou mentindo. Uma mulher como Yukika é ideal como parceira para a vida toda.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17170\t...Guh.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17171\tOuvir uma frase dessas ser dita sem o menor pudor me deixa envergonhado por ter duvidado dele.
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17172\t"D-Desculpa por presumir que você estava só brincando.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17173\t...Mas o que deu em você?[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17174\tVocê não gostava da Saber?"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17175\t"A Saber é como o sol. Não me desperta tanto interesse.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17176\tEla até serviria muito bem como vassala, mas não é adequada para ser a parceira com quem eu passaria o resto da vida."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17177\t"...Você fala umas coisas assustadoras.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17178\tEntão, resumindo, você quer dizer que gosta do fato de a Saegusa ser prendada ou do jeito prestativo dela?"
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17179\t"Ahaha, isso é um mal-entendido, senhor. Não é que Yukika seja prestativa; é que ela é alguém que precisa ser protegida.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17180\tFlores silvestres me interessam mais do que rosas. O quanto você consegue proteger flores simples para que continuem simples... é isso que eu considero o verdadeiro apoio de um homem."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17181\t"..."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17182\tFico sem palavras.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17183\tEm resumo, esse garoto está dizendo que a Saegusa não tem nada de especial, e que isso é justamente a melhor parte dela.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17184\t...O-o que eu faço? Talvez eu acabe gostando mesmo desse sujeito...
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17185\t"Em outras palavras, em vez de controlar quem você ama, a sua maneira de amar é cuidar e proteger?"
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17186\t"O controle só funciona com quem quer ser controlado. As pessoas parecem esquecer isso quando envelhecem. Se eu pudesse escolher, teria preferido ser um bom governante.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17187\t...Sério, por que fui fazer coisas que só serviriam para assustar todo mundo."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17188\tUau...[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17189\tPelo bem do mundo, esse rei devia continuar criança. Com toda certeza. Sem a menor dúvida.
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17190\t"Oh. Mas e se, depois de tudo isso, a pessoa acabar não sendo o seu tipo?[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17191\t[chgfg textoff=0 time=200 storage=ギル子供01a(中)]Cuidar dela significa que você não vai forçá-la a nada, certo?[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17192\tO que pretende fazer se, depois de todo esse cuidado, ela acabar se tornando como a Mestre de quem você não gosta?"
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17193\t"Então eu só a descartaria. Significaria apenas que não era para ser."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17194\t"..."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17195\tRetiro o que eu disse. No fim, ele é o mesmo de sempre.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17196\tEle tem um núcleo implacável que ninguém é capaz de mudar.
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17197\t"...Ah. Então, se a Saegusa acabasse ficando igual à Tohsaka, você deixaria de amá-la?"
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17198\t"Eu não deixaria de amá-la. Só que meu amor por ela não cresceria mais. Ele se tornaria algo que não mudaria pela eternidade. Não aumentaria, mas também não morreria.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17199\tO amor, uma vez obtido, não desaparece. Não existe isso de amar alguém tanto a ponto de começar a odiá-lo.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17200\tIsso só acontece quando um ódio recém-descoberto supera o amor que havia sido acumulado até então."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17201\t"..."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17202\tPor exemplo.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17203\tO garoto que acredita tanto nas partes boas quanto nas partes ruins do ser humano.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17204\tDa mesma forma, ele chega a conhecer um ódio tão grande que todo aquele amor se torna sem valor.
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17205\t"Bem, há casos assim.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17206\tPor mais que um homem se volte contra a humanidade, infelizmente o amor dele continua vivo. Isso faz com que ele pareça humano e, por isso, seja odiado como humano.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17207\tSim. Se ele fosse totalmente inumano, teria sido distinguido como um deus."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17208\tO menino dourado se despede e vira nos calcanhares.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17209\tEle não segue na direção em que Saegusa fugiu, mas sim rumo à ponte que leva para Shinto.
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17210\t"Ei. Você não vai atrás da Saegusa?"[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17211\t"Não precisa. Já consegui o que queria. Yukika se preocupa com os irmãos, então talvez acabe ficando fora até tarde procurando por eles.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17212\tIsso é perigoso, não é? Hoje é o quarto dia, e a ponte à noite é o lugar mais perigoso. No pior cenário, algo irreparável pode acontecer."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17213\t"Mas, graças a você, Yukika foi para casa e não vai voltar aqui até amanhã, no mínimo.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17214\tNão é o ideal, mas é um resultado aceitável."
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17215\tO Rei dos Heróis declara isso com um sorriso impecável e parte de vez.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17216\t"..."[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17217\t...Fiquei sentimental à toa.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17218\tParece que ele está lidando com a própria anormalidade à sua maneira.[lr]
74dt5n077j2p1ngmckdcu7a1ca.epk_dec\t17219\tTalvez ele esteja mesmo descobrindo o valor dessa vida cotidiana tanto quanto eu.
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31518\tO resultado desta batalha depende de conseguirmos neutralizar Fragarach, o trunfo da Mestre inimiga que ainda não conheci.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31519\t"Não, não posso deter Fragarach. É um Fantasma Nobre feito para interceptar outro Fantasma Nobre. Se a enfrentarmos de frente, vamos perder.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31555\t"Algum tipo de Servo. Não é óbvio?"[wm canskip=0]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31556\t"Isso não pode estar certo. Nunca houve um Servo assim antes.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31557\tQue Servo é esse, Avenger?[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31561\tOlhe, Mestre. Depois de ver a nossa presa, você ainda não percebeu nada?"
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31573\t"Claro que sei. Você está aqui para vencer a Guerra do Santo Graal.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31574\tA guerra só termina quando todos os outros Servos forem derrotados.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31607\t"Você me subestima, Servo!"[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31623\tAssim, a maga será destruída pelo Fantasma Nobre inimigo, mesmo que o dela derrote o oponente.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31632\t...significa que, por mais poderoso que seja o Fantasma Nobre do inimigo, ele jamais terá a chance de usá-lo.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31644\tSe existe algo que não perderia para a espada do deus da guerra, seria algo com múltiplas vidas ou um Fantasma Nobre de ressurreição que se ativa automaticamente.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31709\tAssim que seu Nome Verdadeiro foi invocado, Gáe Bolg já carregava em si o resultado de ter atravessado o coração do alvo.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31733\t"Ah... Ei, espera.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31748\tResta apenas o Servo de Bazett, Avenger.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31749\tAgora que perdeu a Mestre, ele provavelmente não é tão forte assim.
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31756\tCada combatente recebeu em cheio o Fantasma Nobre do outro. Lancer não vai sair andando depois disso.
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31763\tDerrotamos Bazett, que acreditávamos ter recriado a Guerra do Santo Graal.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31765\t"Como se isso bastasse. A Guerra do Santo Graal não vai acabar só porque você matou Bazett. Além disso, ela vai voltar à vida enquanto eu continuar por aqui."[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31767\tAvenger continua existindo sem qualquer penalidade aparente, mesmo com sua Mestre morta.
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31778\tOs olhos brilhantes e incandescentes não se voltam apenas para mim, mas também para o Servo.[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31781\t"...Droga. Agora que perdi a minha Mestre, eles acham que eu sou um deles."[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31784\tO Servo me lança um olhar sincero, pedindo ajuda, e...[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31789\tO Servo chamado Avenger derrete por completo, transformando-se em algo parecido com os monstros.
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31792\tEnquanto eu existir, a Guerra do Santo Graal nunca vai terminar."
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31796\t"oUçam. aLcAncem hEaVeN'S fEEL. haH, KeE, haRGh, GERGH, enterrem o vazio. PAREM. Preencham o Santo Graal. PAREM PAREM. Massacrem todas as possibilidades. PAREM PAREM PAREM, eu não consigo ver, eu não consigo ver, eu não consigo ver nada...! iSSo mEsMo, venham me matar, o verdadeiro monstro, PAREM PAREM, fIquem longe, se vocês vierem me matar eu mato vocês...!!!"
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31801\t"                            "[lr]
56jnklgl3nm34g2h62hpj56khs.epk_dec\t31809\tHeaven's Feel. Na Guerra do Santo Graal de meio ano atrás, houve uma garota conhecida por esse nome.[lr]
'''.strip().splitlines()


def build_patches() -> dict[str, dict[str, str]]:
    patches: dict[str, dict[str, str]] = {}
    for raw_line in PATCH_ROWS:
        parts = raw_line.split("\t", 2)
        if len(parts) != 3:
            parts = raw_line.split("\\t", 2)
        if len(parts) != 3:
            raise ValueError(f"Linha de patch inválida: {raw_line!r}")
        file_name, row_id, text = parts
        patches.setdefault(file_name, {})[row_id] = text
    return patches


PATCHES = build_patches()


def parse_rows(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    by_id: dict[str, str] = {}
    by_label: dict[str, str] = {}
    text = path.read_text(encoding="utf-8", errors="replace")

    for line in split_text_lines(text, keepends=False):
        match = ROW_RE.match(line)
        if not match:
            continue
        row_id = match.group("id")
        label = match.group("label")
        row_text = match.group("text")
        by_id.setdefault(row_id, row_text)
        by_label.setdefault(label, row_text)

    return by_id, by_label


def build_clean_lines(file_name: str) -> list[str]:
    en_path = ROOT / "scripts_en" / file_name
    pt_path = ROOT / "scripts_pt-br" / file_name
    overrides = PATCHES[file_name]

    pt_by_id, pt_by_label = parse_rows(pt_path)
    clean_lines = [
        "DAT",
        "id=qid::label=str::text=lstr::",
    ]
    missing: list[str] = []
    unknown_overrides = set(overrides)

    en_text = en_path.read_text(encoding="utf-8", errors="replace")
    for index, line in enumerate(split_text_lines(en_text, keepends=False), start=1):
        if index <= 2:
            continue

        match = ROW_PREFIX_RE.match(line)
        if not match:
            continue

        row_id = match.group("id")
        label = match.group("label")
        text = overrides.get(row_id)
        if text is not None:
            unknown_overrides.discard(row_id)
        else:
            text = pt_by_label.get(label) or pt_by_id.get(row_id)

        if text is None:
            missing.append(f"{file_name}::{row_id}::{label}")
            text = ""

        clean_lines.append(f"{row_id}::{label}::{text}::")

    if unknown_overrides:
        raise ValueError(
            f"Overrides sem linha correspondente em {file_name}: {sorted(unknown_overrides)}"
        )
    if missing:
        raise ValueError("Linhas sem tradução base:\n" + "\n".join(missing))

    return clean_lines


def rebuild_file(file_name: str, stage_dir: Path) -> None:
    en_path = ROOT / "scripts_en" / file_name
    pt_path = ROOT / "scripts_pt-br" / file_name
    clean_lines = build_clean_lines(file_name)
    stage_path = stage_dir / file_name

    stage_dir.mkdir(parents=True, exist_ok=True)
    stage_text = "\n".join(clean_lines) + "\n"
    stage_path.write_text(stage_text, encoding="utf-8")

    rebuilt = rebuild_file_bytes_preserving_structure(
        en_path,
        split_text_lines(stage_text, keepends=True),
    )
    pt_path.write_bytes(rebuilt)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reconstroi scripts Qwen a partir do esqueleto EN, preservando a estrutura crua."
    )
    parser.add_argument(
        "--files",
        nargs="*",
        default=sorted(PATCHES),
        help="Lista de arquivos .epk_dec para aplicar. Padrão: todos deste lote.",
    )
    parser.add_argument(
        "--stage-dir",
        default="_codex_epk_stage",
        help="Pasta para gravar o staging limpo antes do rebuild.",
    )
    args = parser.parse_args()

    stage_dir = ROOT / args.stage_dir

    for file_name in args.files:
        if file_name not in PATCHES:
            raise ValueError(f"Arquivo sem patches neste lote: {file_name}")
        rebuild_file(file_name, stage_dir)
        print(f"[OK] {file_name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
