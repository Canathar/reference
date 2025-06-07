"        _
" __   _(_)_ __ ___  _ __ ___
" \ \ / / | '_ ` _ \| '__/ __|
"  \ V /| | | | | | | | | (__
" (_)_/ |_|_| |_| |_|_|  \___|
"
let mapleader = " "


" =================================================================================================================================
" --                                                         Reference                                                           --
" =================================================================================================================================
" --                                                                                                                             --
" --   For common reference, see the Vim/Vimdiff Cheatsheet                                                                      --
" --      https://gist.github.com/azadkuh/5d223d46a8c269dadfe4                                                                   --
" --                                                                                                                             --
" --   For filter reference, see Vim Filters, External Commands, and the Shell                                                   --
" --      https://vimways.org/2019/vim-and-the-shell/                                                                            --
" --                                                                                                                             --
" --   For tab reference, see Beginners Guide to Tabs in Vim                                                                     --
" --      https://webdevetc.com/blog/tabs-in-vim/                                                                                --
" --                                                                                                                             --
" --   For script creation reference, see the Vimscript Cheatsheet                                                               --
" --      https://github.com/johngrib/vimscript-cheatsheet                                                                       --
" --                                                                                                                             --
" =================================================================================================================================



" =================================================================================================================================
" --                                             Initialize Plugin Manager: Plugged                                              --
" =================================================================================================================================
" --                                                                                                                             --
" --   Quick Reference                                                                                                           --
" --   ---------------                                                                                                           --
" --      :PlugInstall - Install plugins                                                                                         --
" --      :PlugUpdate  - Install or update plugins                                                                               --
" --      :PlugStatus  - Check the status of plugins                                                                             --
" --      :PlugUpdate  - Install or update plugins                                                                               --
" --      :PlugDiff    - Changes since last update                                                                               --
" --                                                                                                                             --
" --   see: https://github.com/junegunn/vim-plug                                                                                 --
" --                                                                                                                             --
" =================================================================================================================================

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

" https://github.com/morhetz/gruvbox
Plug 'morhetz/gruvbox'

" https://github.com/vim-scripts/c.vim
Plug 'vim-scripts/c.vim'

" https://github.com/frazrepo/vim-rainbow
Plug 'frazrepo/vim-rainbow'

" https://github.com/vimwiki/vimwiki
Plug 'vimwiki/vimwiki'

" https://github.com/ryanoasis/vim-devicons
" NOTE1: Always load this plug-in last
" NOTE2: Requires AT LEAST ONE nerd-font from -- https://github.com/ryanoasis/nerd-fonts to be installed
Plug 'ryanoasis/vim-devicons'

call plug#end()



" =================================================================================================================================
" --                                                        Basic Stuff                                                          --
" =================================================================================================================================

   set encoding=utf-8                  " Use unicode instead of latin-1
   set expandtab                       " Use spaces instead of tabs
   set nocompatible                    " Use vim defaults instead of vi defaults
   set nowrap                          " Do not wrap lines
   set number relativenumber           " Show line numbers and show line numbers relative to current line number
   set shiftwidth=3
   set smartindent                     " Do smart indenting when creating a new line
   set spell spelllang=en_us           " Enable the spell checker and set the language/location to English/US
   set textwidth=172                   " Set the maximum column width
   set tabstop=3 softtabstop=3         " Set the number of spaces for a <TAB>



" =================================================================================================================================
" --                                                    Search & Navigation                                                      --
" =================================================================================================================================

   set incsearch                       " Show matches as you type (incrementally)
   set smartcase                       " Override ignorecase if search contains uppercase



" =================================================================================================================================
" --                                                        Appearance                                                           --
" =================================================================================================================================

   syntax on                           " Enable syntax highlighting
   set cursorline                      " Highlight the current line



" =================================================================================================================================
" --                                                   Vimwiki Configuration                                                     --
" =================================================================================================================================

   " General Use Wiki -- Change the default wiki language from vimwiki to markdown
   " Vimwiki Wiki     -- Configure location
   "                     NOTE: Perform the following before use
   "                              cd ~
   "                              git clone https://github.com/vimwiki/vimwikiwiki.git
   let g:vimwiki_list = [
         \ {
            \ 'name': 'General Use Wiki',
            \ 'syntax': 'markdown',
            \ 'ext': 'md'
         \ },
         \ {
            \ 'name': 'Vimwiki Wiki',
            \ 'syntax': 'default',
            \ 'ext': 'wiki',
            \ 'path': '~/vimwikiwiki/wiki',
            \ 'path_html': '~/vimwikiwiki/docs',
            \ 'auto_toc': 1
         \ }
      \ ]

   " Restrict vimwiki to only process the wiki files in the specified path(s)
   let g:vimwiki_global_ext=0



" =================================================================================================================================
" --                                                     Theme Configuration                                                     --
" =================================================================================================================================

   " Configure the display for 256 colors
   set t_Co=256

   " Airline/Powerline/Devicon Plug-in Configuration
   " NOTE: Make sure a nerd-font is installed
   let g:airline_theme="molokai"
   let g:airline_powerline_fonts=1

   " Rainbow Plug-in Configuration
   " NOTE: This plugin is currently interfering with spell checking in text files
   let g:rainbow_active=0

   " Overall Theme / Gruvbox Plug-in Configuration
   " NOTE: Common themes -- desert, elflord
   set background=dark
   let g:gruvbox_italic=1
   let g:gruvbox_transparent_bg=1
   colorscheme gruvbox



" =================================================================================================================================
" --                                                  Display Configuration                                                      --
" =================================================================================================================================
" --                                                                                                                             --
" --   NOTE1: Test the colors by executing the following command                                                                 --
" --             :runtime syntax/colortest.vim                                                                                   --
" --   NOTE2: Set the highlight colors AFTER the colorscheme                                                                     --
" --                                                                                                                             --
" --   Quick Reference                                                                                                           --
" --   ---------------                                                                                                           --
" --      :h cterm-colors - Display color names (16 colors)                                                                      --
" --      :hi[ghlight]    - Display attributes for all current highlight groups                                                  --
" --                                                                                                                             --
" =================================================================================================================================

   " Configure the foreground of comments
   highlight Comment ctermfg=lightblue guifg=lightblue

   " Configure the location and color of the column lines
   set colorcolumn=79,132,172
   highlight ColorColumn ctermbg=brown guibg=brown

   " Configure the background of the current line
   highlight clear CursorLine
   highlight CursorLine ctermbg=darkmagenta

   " Configure the display of the spell checker
   highlight clear SpellBad
   highlight SpellBad cterm=underline ctermul=red

   " Configure the background to be transparent
   highlight Normal ctermbg=NONE guibg=NONE

   " Non-Printable characters (tab: dig >>, trail: dig .M)
   " NOTE1: Enter the characters in insert mode using CTRL+K <char1><char2>
   " NOTE2: Show these characters with :set list
   " NOTE3: Hide these characters with :set nolist
   " see: :help listchars
   set lcs=tab:»_,trail:·,eol:$



" =================================================================================================================================
" --                                                    File/Buffer Handling                                                     --
" =================================================================================================================================

   " Automatically delete all trailing space on save
   autocmd BufWritePre * %s/\s\+$//e

   " Enable Autocompletion
   set wildmode=longest,list,full

   " Enables both filetype detection and filetype plugins which are vimscript files that contain filetype specific commands
   " NOTE: Filetype vimscripts are located in $VIMRUNTIME/ftplugin
   "          (ex: $VIMRUNTIME/ftplugin/xhtml.vim)
   filetype plugin on

   " Hex file read
   nnoremap <silent> <leader>hr :set binary<CR> :%!xxd<CR> :set filetype=xxd<CR>

   " Hex file write
   nnoremap <silent> <leader>hw :set binary<CR> :%!xxd -r<CR> :set filetype=<CR> :noautocmd w<CR>

   " Execute the text in the yank buffer, display the output in a new tab
   " (For Normal/Visual/Select/Operator-pending Modes)
   noremap <leader>x y:tabnew<CR>:r! <C-R>"<CR>

   " Highlight from the cursor to the end of the line, yank the text and paste into terminal
   " (Start in Normal Mode, Enter Visual Mode)
   " NOTE: This macro ONLY works with VIM8
   noremap <leader>v <C-V>$y<C-W><C-W><C-W>""



" =================================================================================================================================
" --                                                 Split/Window Functionality                                                  --
" =================================================================================================================================
" --                                                                                                                             --
" --   see:  :help window-move-cursor                                                                                            --
" --                                                                                                                             --
" =================================================================================================================================

   " Splits open at the bottom and right
   set splitbelow splitright

   " Shortcutting window navigation
   " (For Normal Mode)
   nnoremap <silent> <leader>h :wincmd h<CR>
   nnoremap <silent> <leader>j :wincmd j<CR>
   nnoremap <silent> <leader>k :wincmd k<CR>
   nnoremap <silent> <leader>l :wincmd l<CR>

   " Shortcutting window resizing
   " (For Normal Mode)
   nnoremap <silent> <leader>h+ :resize +5<CR>
   nnoremap <silent> <leader>h- :resize -5<CR>
   nnoremap <silent> <leader>v+ :vertical :resize +5<CR>
   nnoremap <silent> <leader>v- :vertical :resize -5<CR>



" =================================================================================================================================
" --                                                     Tab Functionality                                                       --
" =================================================================================================================================
" --                                                                                                                             --
" --   see: :help tab-page-commands                                                                                              --
" --                                                                                                                             --
" =================================================================================================================================

   " Shortcutting tab creation/destruction
   " (For Normal Mode)
   nnoremap <silent> <leader>tw  :tabnew<CR>
   nnoremap <silent> <leader>tc  :tabclose<CR>
   nnoremap <silent> <leader>tc! :tabclose!<CR>
   nnoremap <silent> <leader>to  :tabonly<CR>
   nnoremap <silent> <leader>to! :tabonly!<CR>

   " Shortcutting tab navigation
   " (For Normal Mode)
   nnoremap <silent> <leader>tp :tabprevious<CR>
   nnoremap <silent> <leader>tn :tabnext<CR>



" =================================================================================================================================
" --                                                  Source Code Search Maps                                                    --
" =================================================================================================================================

   " Git Merge - file search maps
   " (For Normal Mode)
   nnoremap <silent> <leader>lo : /<<<<<<< HEAD<ENTER>
   nnoremap <silent> <leader>br : /=======<ENTER>
   nnoremap <silent> <leader>re : />>>>>>> <ENTER>
   nnoremap <silent> <leader>LO : ?<<<<<<< HEAD<ENTER>
   nnoremap <silent> <leader>BR : ?=======<ENTER>
   nnoremap <silent> <leader>RE : ?>>>>>>> <ENTER>



" =================================================================================================================================
" --                                                 Difference Configuration                                                    --
" =================================================================================================================================
" --                                                                                                                             --
" --   Quick Reference                                                                                                           --
" --   ---------------                                                                                                           --
" --      do           - get change from other to current                                                                        --
" --      dp           - put change from current to other                                                                        --
" --      ]c           - jump to the next change                                                                                 --
" --      [c           - jump to the previous change                                                                             --
" --      zo           - open fold                                                                                               --
" --      zc           - close fold                                                                                              --
" --      zr           - reduce folding level                                                                                    --
" --      zm           - one more folding level                                                                                  --
" --      :diffupdate  - recalculate the diff                                                                                    --
" --      :diffu                                                                                                                 --
" --      :diffg RE    - get from REMOTE                                                                                         --
" --      :diffg BA    - get from BASE                                                                                           --
" --      :diffg LO    - get from LOCAL                                                                                          --
" --                                                                                                                             --
" --   see: :help diff                                                                                                           --
" --                                                                                                                             --
" =================================================================================================================================
if &diff

   " Jump to the next change (forward)
   " (For Normal Mode)
   nnoremap ] ]c

   " Jump to the previous change (backward)
   " (For Normal Mode)
   nnoremap [ [c

   " Colors
   "    Display all the current colors using :hi or a specific group with :hi <group>
   hi DiffAdd    ctermfg=233 ctermbg=LightGreen guifg=#003300 guibg=#DDFFDD gui=none cterm=none
   hi DiffChange ctermbg=LightGray guibg=#ECECEC gui=none cterm=none
   hi DiffDelete ctermfg=233 ctermbg=Red gui=none cterm=none
   hi DiffText   ctermfg=233 ctermbg=yellow guifg=#000033 guibg=#DDDDFF gui=none cterm=none

endif

