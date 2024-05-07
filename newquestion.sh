#!/bin/bash

# Verifica se o argumento do diretório foi fornecido
if [ -z "$1" ]
then
    echo "Por favor, forneça o nome do diretório como argumento."
    exit 1
fi

# Muda para o diretório fornecido
cd "$1"

# Encontra o arquivo com o maior número no nome
max_num=$(ls questoes*.tex | sort -V | tail -n 1 | grep -o '[0-9]\+')

# Incrementa o número
next_num=$((max_num + 1))

# Formata o próximo número para ter dois dígitos
next_num=$(printf "%02d" $next_num)

# Copia o arquivo com o maior número para o novo arquivo
cp "questoes${max_num}.tex" "questoes${next_num}.tex"