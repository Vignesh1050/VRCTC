Note - I couldn't test the retreive booking details part and the race conditions due to lack of time.

--> Overview
A mini version to the IRCTC which allows users to check train availability, seat availability, and book seats. 

--> Tech Stack
- Backend: Python - Flask
- Database: MySQL
- Authentication: JWT-based

--> Included the following requirements
- Register a user(tested successfully)
- Login to the system(tested successfully)
- Giving the ability to the admin to add a new train(tested suucessfully)
- Check if the seats are available in between the desired stations the user wanna travel.(tested successfully)
- Book a seat if available(tested but getting error in the token)

-->Steps to set-up
- Create a database
- Add the database credentials- API KEY AND JWT
- Create the files for database connection, authorization , models , routes and save them in a single directory.
- Start the server.

-->Steps to Test (Tested using cmd itself, not postman)
1)Test the API server 
2)Test API endpoints;
  -Register user 
  ##Example -
   C:\Users\nvign> $headers = @{
>>     "Content-Type" = "application/json"
>> }
PS C:\Users\nvign> $body = '{"username": "Vignesh", "password": "Vignesh@0305", "role": "user"}'
PS C:\Users\nvign>
PS C:\Users\nvign> Invoke-WebRequest -Uri "http://127.0.0.1:5000/register" -Method POST -Headers $headers -Body $body
StatusCode        : 201
StatusDescription : CREATED
Content           : {
                      "message": "User registered successfully!"
                    }

RawContent        : HTTP/1.1 201 CREATED
                    Connection: close
                    Content-Length: 49
                    Content-Type: application/json
                    Date: Thu, 30 Jan 2025 04:04:26 GMT
                    Server: Werkzeug/3.1.3 Python/3.12.1

                    {
                      "message": "User registere...
Forms             : {}                                                                                                  Headers           : {[Connection, close], [Content-Length, 49], [Content-Type, application/json], [Date, Thu, 30 Jan                        2025 04:04:26 GMT]...}                                                                              Images            : {}                                                                                                  InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 49
-- This wway rest of the following endpoint or API requests can be tested
-Login and Toke for user
-Testing user features like availability of trains and seats.
-And finally seat booking.
-Testing the add train option which would be in hands of the admin.

##Note - No adiotional testes were done. 
  







