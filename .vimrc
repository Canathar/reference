"        _
" __   _(_)_ __ ___  _ __ ___
" \ \ / / | '_ ` _ \| '__/ __|
"  \ V /| | | | | | | | | (__
"   \_/ |_|_| |_| |_|_|  \___|

let mapleader = " "

" =================================
" ---------- Basic Stuff ----------
" =================================
   syntax on

   set encoding=utf-8
   set tabstop=3 softtabstop=3
   set shiftwidth=3
   set expandtab
   set smartindent
   set number relativenumber

   set nowrap
   set smartcase


" ===========================================
" ---------- Display Configuration ----------
" ===========================================
   colorscheme desert
   "colorscheme elflord
   set colorcolumn=132
   highlight ColorColumn ctermbg=lightgrey guibg=lightgrey


" ===================================
" ---------- File Handling ----------
" ===================================

   " Automatically delete all trailing space on save
   autocmd BufWritePre * %s/\s\+$//e

   " Enable Autocompletion
   set wildmode=longest,list,full


" ================================================
" ---------- Split/Window Functionality ----------
" ================================================

   " Splits open at the bottom and right
   set splitbelow splitright

   " Shortcutting window navigation
   nnoremap <silent> <leader>h :wincmd h<CR>
   nnoremap <silent> <leader>j :wincmd j<CR>
   nnoremap <silent> <leader>k :wincmd k<CR>
   nnoremap <silent> <leader>l :wincmd l<CR>

   " Shortcutting window resizing
   nnoremap <silent> <leader>+ :resize +5<CR>
   nnoremap <silent> <leader>- :resize -5<CR>


" =================================
" ---------- Search Maps ----------
" =================================

   " Git Merge - file search maps
   map <silent> <leader>lo : /<<<<<<< HEAD<ENTER>
   map <silent> <leader>br : /=======<ENTER>
   map <silent> <leader>re : />>>>>>> <ENTER>
   map <silent> <leader>LO : ?<<<<<<< HEAD<ENTER>
   map <silent> <leader>BR : ?=======<ENTER>
   map <silent> <leader>RE : ?>>>>>>> <ENTER>


" ==============================================
" ---------- Difference Configuration ----------
" ==============================================
if &diff

   " Location Marker
   set cursorline

   " Next Difference (forward)
   map ] ]c

   " Next Difference (backward)
   map [ [c

endif

