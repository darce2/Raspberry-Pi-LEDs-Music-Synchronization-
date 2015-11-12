#include<unistd.h>

main (int argc, char** argv) {

   pid_t childpid;
   while(1) {
      childpid = fork();
      if (childpid) {

         wait(NULL);
      } else {
           execvp(argv[1], &argv[1]);
           break;
        }
   }
}

