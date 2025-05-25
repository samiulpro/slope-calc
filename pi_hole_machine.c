#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <time.h>
#include <unistd.h>

void logging(const char message[])
{
    FILE *server_boot_log;
    server_boot_log = fopen("pi_hole_machine_log.txt", "w");
    fprintf(server_boot_log, "%s", message);
    fclose(server_boot_log);
}

const char* time_stamp() {
    char time_buffer[264];
    time_t current_time;
    char* time_string;

    current_time = time(NULL);
    if (current_time == ((time_t)-1)) {
        exit(EXIT_FAILURE);
    }

    time_string = ctime(&current_time);
    if (time_string == NULL) {
        exit(EXIT_FAILURE);
    }
    // Dynamically allocating the time string
    char* result = malloc(strlen(time_string) + 1);
    if (result == NULL){
        exit(EXIT_FAILURE);
    }

    strcpy(result, time_string);
    return result;
}

int main(void)
{
    char command[512];
    char message[512];
    snprintf(command, sizeof(command), "Vboxmanager vmstart pi_hole_machine --headless");
    // Starting the command
    int status = system(command);
    sleep(50000);
    if (status == 0)
    {
        snprintf(message, sizeof(message), "[%s] Fuck you\n", time_stamp());
        logging(message);
        memset(message, 0, sizeof(message));
    }
    else
    {
        snprintf(message, sizeof(message), "[%s] Fuck you again %d\n", time_stamp(), status);
        logging(message);
        memset(message, 0, sizeof(message));
    }
    

    exit(0);
}