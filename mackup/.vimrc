" Not compatible with vi 
set nocompatible

"----------------------- Vim Plug -------------------------
" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

" ---- Themes ----
Plug 'crusoexia/vim-monokai'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

"----  Common ----
Plug 'scrooloose/nerdtree'
Plug 'jistr/vim-nerdtree-tabs'
Plug 'vim-syntastic/syntastic'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'vim-scripts/a.vim'
Plug 'nathanaelkane/vim-indent-guides'
Plug 'scrooloose/nerdcommenter'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'airblade/vim-gitgutter'

Plug 'rdnetto/YCM-Generator', { 'branch': 'stable' }

Plug 'Valloric/YouCompleteMe', { 'do': './install.py --clangd-completer' }

"------ Cpp -------
Plug 'octol/vim-cpp-enhanced-highlight', { 'for': 'cpp' }

" Initialize plugin system
call plug#end()

"------------------- Common Setting  ------------------------
" Backspace setting
set backspace=indent,eol,start
" Show cursor position.
set ruler
" Show line number.
set number
" Show cursor's line and column. 
set cursorline
set cursorcolumn
" Show command.
set showcmd
" Incremental search
set incsearch
" Highlight search results.
" Clear highlight with,
" :nohlsearch
set hlsearch
" Command line completeion.
set wildmenu
" No blink cursor.
set gcr=a:block-blinkon0
" No GUI.
set guioptions-=l
set guioptions-=L
set guioptions-=r
set guioptions-=R
set guioptions-=m
set guioptions-=T
" Indent based on filetype.
filetype indent on
" Expand tab to whitespace.
set expandtab
" Indent
let default_indent=4
let &tabstop=default_indent
let &softtabstop=default_indent
" Shift width.
let &shiftwidth=default_indent
" Fold based on syntax. 
set foldmethod=indent
" No fold at startup.
set foldlevelstart=99
" No line wrapping. 
set nowrap
" Syntax coloring.
syntax on
" Use mouse. 
set mouse=a
" Clear line number column color.
highlight clear SignColumn

"---------------- Shortcut Mapping -------------------
" Buffer previous/next.
nmap <leader>bp :bp<CR>
nmap <Leader>bn :bn<CR>
if has('linux')
    " Copy to clipboard.
    vnoremap <Leader>y "+y
    " Paste from clipboard.
    nmap <Leader>p "+p
else
    " Copy to clipboard.
    vnoremap <Leader>y "*y
    " Paste from clipboard.
    nmap <Leader>p "*p
endif
" Write buffer.
nmap <Leader>w :w<CR>
" Close window.
nmap <Leader>q :q<CR>

"--------------------- Plugin Setting ----------------------

"---- Theme ----
set background=dark
try
  colorscheme monokai
catch
endtry

"---- vim-airlines ----
" Show status. 
set laststatus=2

" Fancy arrow symbols.
set encoding=utf-8
set guifont=Ubuntu\ Mono\ derivative\ Powerline:h16
let g:airline_powerline_fonts=1
let g:airline_detect_paste=1
let g:airline#extensions#tabline#enabled =1
let g:airline_theme='molokai'

"---- vim-nerdtree-tabs ----
" Toggle NerdTree.
nmap <silent><leader>t :NERDTreeTabsToggle<CR>
let g:nerdtree_tabs_open_on_console_startup=0

"---- syntastic settings ----
let g:syntastic_error_symbol='✘'
let g:syntastic_warning_symbol="▲"
augroup mySyntastic
  au!
  au FileType tex let b:syntastic_mode="passive"
augroup END

"---- vim-gitgutter ----
let g:airline#extensions#hunks#non_zero_only=1

"---- vim-indent-guide ----
let g:indent_guides_enable_on_vim_startup=1
let g:indent_guides_start_level=2
let g:indent_guides_guide_size=1
nmap <silent> <Leader>i <Plug>IndentGuidesToggle

"----  YouCompleteMe ----
" Global config.
let g:ycm_global_ycm_extra_conf = '~/.ycm_extra_conf.py'
" Menu.
highlight Pmenu ctermfg=0 ctermbg=33 guifg=#005f87 guibg=#EEE8D5
highlight PmenuSel ctermfg=0 ctermbg=33 guifg=#AFD700 guibg=#106900
" Completion in comments.
let g:ycm_complete_in_comments=1
" Allow load config without confirm.
let g:ycm_confirm_extra_conf=0
" Completion from tags. 
let g:ycm_collect_identifiers_from_tags_files=1
" STD tags 
set tags+=/data/misc/software/misc./vim/stdcpp.tags
" Only list. 
set completeopt-=preview
" No cache. 
let g:ycm_cache_omnifunc=1
" Syntax.         
let g:ycm_seed_identifiers_with_syntax=1
" YCM FixIt.
map <F9> :YcmCompleter FixIt<CR>
" Jump. 
nnoremap <leader>jc :YcmCompleter GoToDeclaration<CR>
nnoremap <leader>jd :YcmCompleter GoToDefinition<CR>
" Interpreter
let g:ycm_python_binary_path = 'python3'

" ----- delimitMate -----
let delimitMate_expand_cr=1
augroup mydelimitMate
    au!
    au FileType markdown let b:delimitMate_nesting_quotes = ["`"]
    au FileType tex let b:delimitMate_quotes = ""
    au FileType tex let b:delimitMate_matchpairs = "(:),[:],{:},`:'"
    au FileType python let b:delimitMate_nesting_quotes = ['"', "'"]
augroup END

" ---- UltiSnip ----
let g:UltiSnipsExpandTrigger="<leader><tab>"
let g:UltiSnipsJumpForwardTrigger="<leader><tab>"
let g:UltiSnipsJumpBackwardTrigger="<leader><s-tab>"

" ---- vim-cpp-enhanced-highlight ---
let g:cpp_class_scope_highlight = 1
let g:cpp_member_variable_highlight = 1
let g:cpp_class_decl_highlight = 1
let g:cpp_experimental_simple_template_highlight = 1
let g:cpp_concepts_highlight = 1
