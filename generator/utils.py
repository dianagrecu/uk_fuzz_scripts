from templates import *

c_extension = ".c"
string_prefix = "str:"
gen_prefix = "gen_"

gen_dict = {
    "gen_isupper":  gen_isupper,
    "gen_malloc":   gen_malloc,
    "gen_memset":   gen_memset,
    "gen_open":     gen_open,
    "gen_read":     gen_read,
    "gen_strncpy":  gen_strncpy,
    "gen_write":    gen_write
}

# to compile unikraft as lib
# ar rc libukstatic.a $(find build -mindepth 1 -maxdepth 1 -type f -regex '.*/lib[^\.]+.o$')


# to compile the program linked with unikraft so

# gcc -L. -nostdinc -nostdlib -Wl,--build-id=none -g -no-pie  -Wl,-e,
# liblinuxuplat_start /home/diana/Documents/licenta/unikraft/apps/helloworld/build/genericapp.o -Wl,-T,
# /home/diana/Documents/licenta/unikraft/apps/helloworld/build/liblinuxuplat/link64.lds -Wl,-T,
# /home/diana/Documents/licenta/unikraft/unikraft/lib/ukdebug/extra.ld -Wl,-T,
# /home/diana/Documents/licenta/unikraft/unikraft/lib/vfscore/extra.ld -o app.git_linuxu-x86_64.dbg -lukstatic
app_unikraft_so = "gcc -L. -nostdinc -nostdlib -Wl,--build-id=none -g -no-pie  -Wl,-e,_liblinuxuplat_start " \
                  "/home/diana/Documents/licenta/unikraft/apps/helloworld/build/genericapp.o -Wl,-T," \
                  "/home/diana/Documents/licenta/unikraft/apps/helloworld/build/liblinuxuplat/link64.lds -Wl,-T," \
                  "/home/diana/Documents/licenta/unikraft/unikraft/lib/ukdebug/extra.ld -Wl,-T," \
                  "/home/diana/Documents/licenta/unikraft/unikraft/lib/vfscore/extra.ld -o " \
                  "app.git_linuxu-x86_64.dbg -lukstatic "
