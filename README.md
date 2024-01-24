Detalii aplicatie testata: 
Scop: Simulează un API simplu pentru a furniza informații despre postări, comentarii, sarcini și utilizatori.
Sursa datelor: Datele sunt simulate și returnate de la https://jsonplaceholder.typicode.com.

Structura aplicației:

Request-uri
Am creat mai multe clase de request-uri, fiecare având metode specifice pentru interacțiunea cu diferite endpoint-uri ale API-ului JSONPlaceholder.

PostsRequest
Metode pentru obținerea tuturor postărilor și a unei postări specifice prin ID, precum și pentru crearea unei noi postări.

CommentsRequest
Metode pentru obținerea tuturor comentariilor și a comentariilor specifice pentru un post prin ID-ul postului.

TodosRequest
Metode pentru obținerea tuturor todo-urilor și a unui todo specific prin ID.

UsersRequest
Metode pentru obținerea tuturor utilizatorilor și a unui utilizator specific prin ID.

GeneralRequests
Metode pentru request-uri generale, cum ar fi accesarea unui endpoint inexistent și verificarea timpului de răspuns pentru un endpoint valid.

Teste
Pentru fiecare set de request-uri, am creat teste corespunzătoare pentru a verifica funcționalitatea și performanța API-ului.

Teste pentru PostsRequest
Teste pentru obținerea tuturor postărilor, crearea unui post și obținerea unui post specific.

Teste pentru CommentsRequest
Teste pentru obținerea tuturor comentariilor și a comentariilor filtrate după postID.

Teste pentru TodosRequest
Teste pentru obținerea tuturor todo-urilor și a unui todo specific.

Teste pentru UsersRequest
Teste pentru obținerea tuturor utilizatorilor și a unui utilizator specific.

Teste Generale (TestGeneral)
Test pentru verificarea răspunsului la o cerere la un endpoint inexistent și test pentru verificarea timpului de răspuns la un endpoint valid.
