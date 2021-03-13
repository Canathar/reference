let mapleader = " "

" Basic Stuff
   syntax on

   set encoding=utf-8
   set tabstop=3 softtabstop=3
   set shiftwidth=3
   set expandtab
   set smartindent
   set number relativenumber

   set nowrap
   set smartcase


" Display configuration
   colorscheme desert
   "colorscheme elflord
   set colorcolumn=132
   highlight ColorColumn ctermbg=lightgrey guibg=lightgrey


" Automatically delete all trailing space on save
   autocmd BufWritePre * %s/\s\+$//e


" Enable Autocompletion
   set wildmode=longest,list,full


" Split functionality
   set splitbelow splitright
   nnoremap <C-H> <C-W><C-H>
   nnoremap <C-J> <C-W><C-J>
   nnoremap <C-K> <C-W><C-K>
   nnoremap <C-L> <C-W><C-L>


" Git Merge - file search maps
   map lo : /<<<<<<< HEAD<ENTER>
   map br : /=======<ENTER>
   map re : />>>>>>> <ENTER>
   map LO : ?<<<<<<< HEAD<ENTER>
   map BR : ?=======<ENTER>
   map RE : ?>>>>>>> <ENTER>


" Difference configuration
if &diff

   " Location Marker
   set cursorline

   " Next Difference (forward)
   map ] ]c

   " Next Difference (backward)
   map [ [c


endif

