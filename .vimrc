"        _
" __   _(_)_ __ ___  _ __ ___
" \ \ / / | '_ ` _ \| '__/ __|
"  \ V /| | | | | | | | | (__
"   \_/ |_|_| |_| |_|_|  \___|

let mapleader = " "

" For script creation reference, see the Vimscript Cheatsheet
" https://github.com/johngrib/vimscript-cheatsheet

" ========================================================
" ---------- Initialize Plugin Manager: Plugged ----------
" ========================================================
" -- Quick Reference                                    --
" -- ---------------                                    --
" --    :PlugInstall - Install plugins                  --
" --    :PlugUpdate  - Install or update pluigns        --
" --    :PlugStatus  - Check the status of plugins      --
" --    :PlugUpdate  - Install or update pluigns        --
" --    :PlugDiff    - Changes since last update        --
" ========================================================
" see: https://github.com/junegunn/vim-plug

" Check to see if Plugged is downloaded
let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))

   " Download Plugged
   silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

   " Install Plugged and all plugins
   autocmd VimEnter * PlugInstall --sync | source $MYVIMRC

endif

" Activate Plugged
call plug#begin('~/.vim/plugged')

" https://github.com/vim-airline/vim-airline
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" https://github.com/vim-scripts/CharTab
Plug 'vim-scripts/CharTab'

call plug#end()


" =================================
" ---------- Basic Stuff ----------
" =================================
   syntax on

   set encoding=utf-8
   set textwidth=132
   set tabstop=3 softtabstop=3
   set shiftwidth=3
   set expandtab
   set smartindent
   set number relativenumber

   set nowrap
   set smartcase

   set incsearch


" ===========================================
" ---------- Display Configuration ----------
" ===========================================
   colorscheme desert
   "colorscheme elflord
   set colorcolumn=132
   highlight ColorColumn ctermbg=lightgrey guibg=lightgrey

   " Non-Printable characters (tab: dig >>, trail: dig .M)
   set lcs=tab:»_,trail:·


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
   nnoremap <silent> <leader>h+ :resize +5<CR>
   nnoremap <silent> <leader>h- :resize -5<CR>
   nnoremap <silent> <leader>v+ :vertical :resize +5<CR>
   nnoremap <silent> <leader>v- :vertical :resize -5<CR>


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


   " Colors
   "    Display all the current colors using :hi or a specific group with :hi <group>
   hi DiffAdd    ctermfg=233 ctermbg=LightGreen guifg=#003300 guibg=#DDFFDD gui=none cterm=none
   hi DiffChange ctermbg=LightGray guibg=#ECECEC gui=none cterm=none
   hi DiffDelete ctermfg=233 ctermbg=Red gui=none cterm=none
   hi DiffText   ctermfg=233 ctermbg=yellow guifg=#000033 guibg=#DDDDFF gui=none cterm=none

endif
