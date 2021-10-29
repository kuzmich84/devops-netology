# devops-netology
Netology course DevOps 2021 

##Ответы на задание №1 занятия «2.1. Системы контроля версий.»

`**/.terraform/*`  
Игнорируются любые файлы, которые находятся в каталоге .terraform, который в свою очередь может находится либо в корневом каталоге, либо в каталоге 1 уровня от корневого

`*.tfstate`  
Игнорируются файлы с расширением .tfstate, расположенные в любом месте репозитория 

`*.tfstate.*`  
Игнорируются файлы, которые в середине именования файла имеют значение .tfstate., либо имеют название равное .tfstate.,   расположенные в любом месте репозитория. * - любое количество символов или нуль

`crash.log ` 
Игнорируется файл crash.log, расположенный в любом месте репозитория

`*.tfvars`
Игнорируются файлы с расширением *.tfvars,   расположенные в любом месте репозитория 

`override.tf`  
Игнорируется файл override.tf , расположенный в любом месте репозитория

`override.tf.json `
Игнорируется файл override.tf.json , расположенный в любом месте репозитория


`*_override.tf`
Игнорируются файлы, наименования которых заканчивается на _override.tf, либо называются как _override.tf,  расположенных в любом месте репозитория. * - любое количество символов или нуль

`*_override.tf.json`
Игнорируются файлы, наименования которых заканчивается на _override.tf.json, либо называются как _override.tf.json, расположенных любом месте репозитория. * - любое количество символов или нуль

`.terraformrc `
Игнорируется файл .terraformrc, расположенный в любом месте репозитория

`terraform.rc `
Игнорируется файл terraform.rc , расположенный в любом месте репозитория

Выполняю задние 3 блока "2.2. Основы Git"  
Выполняю адание 4 – Упрощаем себе жизнь  блока "2.2. Основы Git"