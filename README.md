# Trabalho_software
Trabalhinho topzão Pomodoro
### Concepção: 
* O público que visamos atingir são aqueles que buscam ter uma maior produtividade. Com ele o gerenciamento do tempo utilizado é aperfeiçoado, facilitando a organização do usuário para começar e finalizar atividades do dia a dia. 
* O software vai controlar o tempo de trabalho, 25 minutos, e o de descanso, 5 minutos, do usuário emitindo um aviso no display. 
### Levantamentos: 
* Ao final do projeto visamos obter um pomodoro que mande uma notificação a cada 25 minutos de trabalho intervalado por outros 5 minutos de descanso (que ao final deste intervalo também notifica que o tempo de descanso acabou). 
* Expectativas: fazer um código limpo, simples e que entregue o que o projeto propõe. Objetivos prioritários: sermos capazes de recriar o pomodoro a sua forma tradicional, com 25 minutos em que o usuário se dedicara a uma atividade e 5 minutos de descanso. 
* Expectativas do gerente de projeto: entregar um produto que cumpra os requisitos desejados, recriar o pomodoro. 
* Expectativas da equipe desenvolvimento: aprofundar os conhecimentos da equipe em Python e Micropython. 
* [link_para_projeto](micropython.py)
### Sprints: <br />
1.Concepção inicial apenas da parte do temporizador, estudo da biblioteca “time”, levamos um dia para implementar esta funcionalidade. <br />
2.Concepção inicial das mensagens exibidas na tela do microcontrolador, estudo das bibliotecas “machine” e “ framebuf”, levamos um dia para implementar. <br />
3.União dos scripts criando um pomodoro funcional, lavamos dois dias para esta implementação. Dificuldade na organização do script. <br />
4.Otimização e organização do código para potencial ganho de escala e maior eficiência em possíveis manutenções, além de adição da funcionalidade que mostra na tela o ciclo do pomodoro que o usuário está, levamos dois dias para implementar corretamente. Dificuldade para conceber onde colocar as configurações padrão da tela dentro do objeto "pomodoro".
### Diagrama UML:
<img src = "imgs/Diagrama_UML.png">