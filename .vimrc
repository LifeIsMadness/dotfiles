syntax on
filetype plugin indent on
set shiftwidth=4
set softtabstop=4
set tabstop=4
set expandtab
set number
set showmatch 

" Colorscheme
colorscheme slate

" Always show the status line
set laststatus=2
" Format the status line
set statusline=%F\ %{FugitiveStatusline()}\ \ Line:\ %l\ Column:\ %c

" yml files, 2 spaces
autocmd Filetype yml setlocal ts=2 sw=2 expandtab
autocmd Filetype yaml setlocal ts=2 sw=2 expandtab

