##Na pasta ```presentation``` será possível encontrar a apresentação do Pitch.##

# Valentina
Somos a Valentina, um sistema criado para ajudar na prevenção de casos de violência doméstica. A partir de uma base de dados (DataSenado), identificamos características de mulheres que já sofreram violência doméstica, e criamos um modelo que prevê se uma mulher pode estar em situação de risco. Assim, oferecemos informação e suporte já no início do problema.

Este repositório está dividido em três partes:
* Na pasta ```bot``` você encontrará os códigos referente ao chatbot desenvolvido para acolhimento das mulheres e coleta de dados relacionados a possiveis agressões que possam ter ocorrido;
* Na pasta ```model_training``` estão os códigos relacionados ao classificador probabilístico baseado em Random Forest utilizado para predizer a probabilidade da mulher estar em situação de violência e também você encontrará as bases de dados utilizadas para o treinamento do classificador;
* Na pasta ```model_api``` você encontrará a api responsável por fazer a comunicação do cliente com o classificador desenvolvido.
