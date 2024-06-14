# project-4

Name: Jordan Woodard

Overview: This is a school project for a paper trading app that I made called "General Banks". The overall theme of the app is based on the military, and the general idea is that you as the user are a "soldier" who is "serving" in the "army" to "fight" a "war" in order to manage your finances.

Details: General Banks features a charting library known as "Matplotlib", which it uses to track stock data.  Five pages make up the project in total.  However, only three of them (Home, Login, and Portfolio) are accessible, since the other two (Contact and Settings) are not.  The links used for page navigation are on the top right side of the navbar.  It is possible to move between the Home page and Login page by clicking the links.  As for the Portfolio page, you can go there from the Login page by pressing a button, and you can go back to the Login page by clicking a link on the Portfolio page.  A graph and a table can be found on the Portfolio page, and they are both set up to track stock data for 2024.  In addition, each page features an audio panel near the bottom that plays a unique music track.  The music is set to play automatically and will loop when the track reaches the end, but you can pause or mute it if you don't want to listen to it.

Technologies: html, css, py, pyscript

Improvements: spend more time writing Python code, use Django to build a website, try out different charting libraries

<!DOCTYPE html>

<html lang="en">

    <head>

        <title>General Banks</title>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Saira+Stencil+One&display=swap" rel="stylesheet">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <link rel="stylesheet" href="./css/template.css">

    </head>

    <body class="home-background">

        <nav class="navbar">
            <div class="row">
                <div class="col-2">
                    <img src="./images/soldier2.jpg" height="180" alt="army general">
                </div>
                <div class="navbar-brand col-6">
                    <header>General Banks</header>
                </div>
                <div class="col-3">
                    <ul class="nav">
                        <li class="nav-item">
                          <a class="nav-link active" aria-current="page" href="./login.html">Report for duty (Login)</a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link disabled" aria-disabled="true">Talk to command (Contact)</a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link disabled" aria-disabled="true">Change your combat gear (Settings)</a>
                        </li>
                      </ul>
                </div>
            </div>
        </nav>

        <div class="container text-center">
            <div class="row">
                <div class="col-4">
                    <img src="./images/army_squad5.jpg" height="180" alt="home squad">
                </div>
                <div class="col-4 my-auto">
                    <h1 class="header">HOME</h1>
                </div>
                <div class="col-4">
                    <img src="./images/army_squad5.jpg" height="180" alt="home squad">
                </div>
            </div>
        </div>

        <div class="container">
            <h3 class="header">Orientation</h3>
            <p>Atten-chun!  Welcome to the frontline, soldier.  We at the UBF (or the "United Banking Federation") are happy to 
                recruit you.
            </p>
  
            <h3 class="header">Purpose</h3>
            <p>General Banks is an app designed to help soldiers like you keep their finances in order.  You can track your 
                stocks, make investments, and send transactions, all from the comfort of whatever base you're stationed at.  
                As all properly trained soldiers know, preparation and discipline are key to winning any battle.
            </p>
 
            <h3 class="header">Mission Debriefing</h3>
            <p>One of the United Banking Federation's five military branches, the UBF army understands that saving money is 
                a war that you must fight for the rest of your life, so the men and women who proudly serve the UBF are willing 
                to make the ultimate sacrifice to protect our country from bankruptcy, money theft, loss of stock, and all 
                other financial threats.  General Banks will lead you and your fellow comrades to victory.  We salute you, 
                soldier.
            </p>
        </div>

        <div class="container text-center">
            <img src="./images/emblem2.jpg" alt="company logo" class="my-2">
            <section>
                <audio controls autoplay loop>
                    <source src="./audio/army-157045.mp3" type="audio/mpeg">
                    <!--<source src="./audio/epic-cinematic-patriotic-155914.mp3" type="audio/mpeg">-->
                </audio>
            </section>
            <p>United Banking Federation:  proud to serve your finances</p>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>

    </body>

</html>
