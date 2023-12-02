<template>
  <div class="about-container">
    <div class="text-h4" style="color: white">About</div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">UMBINAAM</span> — Ultimately Meaningless
      But Interesting Nonetheless Aggregate Advanced Metric. We use existing
      advanced stats (listed below) as inputs into a weighted algorithm that
      considers each metric's strengths and flaws, as well as their respective
      inputs. Each stat leans into certain metrics more than others (e.g. Box
      Score numbers, On/Off +/-, etc.), and these weights are also adjusted then
      applied within the algorithm. Ultimately, UMBINAAM values should be viewed
      similarly to traditional Z-Scores, where +/- 1.0 is exactly 1 standard
      deviation away from a replacement level NBA player (UMBINAAM = 0.0), from
      a holistic evaluation standpoint. Stats are updated daily.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">EPM</span> — Estimated Plus Minus. EPM
      is a stat created and maintained by
      <a href="https://www.dunksandthrees.com/">DunksAndThrees</a>. To read more
      about EPM and its derivation, as well as conclusive oEPM and dEPM numbers,
      visit
      <a href="https://dunksandthrees.com/blog/metric-comparison/">About EPM</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">RAPTOR</span> — A stat created and
      maintained by
      <a
        href="https://projects.fivethirtyeight.com/2023-nba-player-projections/"
        >FiveThirtyEight</a
      >. Unfortunately, FiveThirtyEight has retired the RAPTOR metric as of
      2023-24. To read more about RAPTOR and its derivation, as well as
      historical stats up to 2023, visit
      <a href="https://projects.fivethirtyeight.com/nba-player-ratings/"
        >RAPTOR</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">DPM</span> — Also known as DARKO. A stat
      created and maintained by
      <a href="https://nbastuffer.com/">NBAStuffer</a> — DARKO, aka Daily
      Plus-Minus or DPM, is created by Kostya Medvedovsky. DARKO (stands for
      “Daily Adjusted and Regressed Kalman Optimized“) is a composite predictive
      metric that uses box score and plus-minus stats. By blending these
      components in proportion to the number of total possessions of a player,
      recent performance is weighted more heavily to better predict future game
      outcomes. To read more about DARKO, visit
      <a href="https://www.nbastuffer.com/analytics101/darko-daily-plus-minus/"
        >DARKO Daily Plus Minus</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">BPM</span> — Box Plus/Minus, a stat
      created and maintained by
      <a href="https://basketball-reference.com/">Basketball Reference</a> — Box
      Plus/Minus, Version 2.0 (BPM) is a basketball box score-based metric that
      estimates a basketball player's contribution to the team when that player
      is on the court. It is based only on the information in the traditional
      basketball box score--no play-by-play data or non-traditional box score
      data (like dunks or deflections) are included. To read more about BPM,
      visit
      <a href="https://www.basketball-reference.com/about/bpm2.html"
        >About BPM</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">VORP</span> — Value Over Replacement
      Player (available since the 1973-74 season in the NBA); a box score
      estimate of the points per 100 TEAM possessions that a player contributed
      above a replacement-level (-2.0) player, translated to an average team and
      prorated to an 82-game season. Multiply by 2.70 to convert to wins over
      replacement. To learn more, visit
      <a href="https://www.basketball-reference.com/about/bpm2.html"
        >BasketballReference</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">LEBRON</span> — Luck-adjusted player
      Estimate using a Box prior Regularized ON-off. Put simply, LEBRON
      evaluates a player's contributions using the box score (weighted using
      boxPIPM's weightings stabilized using Offensive Archetypes) and advanced
      on/off calculations (using Luck-Adjusted RAPM methodology) for a holistic
      evaluation of player impact per 100 possessions on-court. To read more
      about LEBRON, visit
      <a href="https://www.bball-index.com/lebron-introduction/"
        >Basketball Index</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">WS/48</span> — Win Shares Per 48 Minutes
      (available since the 1951-52 season in the NBA); an estimate of the number
      of wins contributed by the player per 48 minutes (league average is
      approximately 0.100). Please see the article Calculating Win Shares for
      more information.
      <a href="https://www.basketball-reference.com/about/ws.html">About WS</a>.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">PIE</span> —Player Impact Estimate aka
      PIE, is a metric to gauge a player’s all-around contribution to the game.
      Almost all statistical categories in the box score are involved in the PIE
      formula. PIE answers what % of the events in a game each player
      contributed. <br />PIE Formula=(PTS + FGM + FTM – FGA – FTA + Deff.REB +
      Off.REB/2 + AST + STL + BLK/2 – PF – TO) / (Game.PTS + Game.FGM + Game.FTM
      – Game.FGA – Game.FTA + Game.Deff.REB + Game.Off.REB/2 + Game.AST +
      Game.STL + Game.BLK/2 – Game.PF – Game.TO). To read more, visit
      <a
        href="https://www.nbastuffer.com/analytics101/player-impact-estimate-pie/"
        >Player Impact Estimate</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">PIE</span> — Player Impact Estimate aka
      PIE, is a metric to gauge a player’s all-around contribution to the game.
      Almost all statistical categories in the box score are involved in the PIE
      formula. PIE answers what % of the events in a game each player
      contributed. <br />PIE Formula=(PTS + FGM + FTM – FGA – FTA + Deff.REB +
      Off.REB/2 + AST + STL + BLK/2 – PF – TO) / (Game.PTS + Game.FGM + Game.FTM
      – Game.FGA – Game.FTA + Game.Deff.REB + Game.Off.REB/2 + Game.AST +
      Game.STL + Game.BLK/2 – Game.PF – Game.TO). To read more, visit
      <a
        href="https://www.nbastuffer.com/analytics101/player-impact-estimate-pie/"
        >Player Impact Estimate</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">RPM</span> — Real Plus-Minus shares a
      family resemblance with the traditional +/- stat in the box score, which
      merely registers the net change in score (plus or minus) while each player
      is on the court. RPM estimates how many points each player adds or
      subtracts, on average, to his team's net scoring margin for each 100
      possessions played. The RPM model also yields separate ratings for the
      player's impact on both ends of the court: offensive RPM (ORPM) and
      defensive RPM (DRPM). To read more about RPM, visit
      <a
        href="https://www.espn.com/nba/story/_/id/10740818/introducing-real-plus-minus"
        >NBA's Introducion Real Plus-Minus</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">WPA</span> — Win Probability Added, a
      stat created and maintained by Inpredictable. Win Probability Added aka
      WPA, utilizes box score stats to rank player contributions which are
      weighted to give more credit to clutch shots and pace of the game. Created
      by Mike Beuoy in 2014, WPA focuses on missed shots, made shots, turnovers,
      and free throws while ignoring rebounds, assists, blocks and steals in
      clutch minutes or in garbage time. To read more, visit
      <a href="http://stats.inpredictable.com/nba/ssnPlayer.php"
        >NBA Win Probabiliy Added</a
      >.
    </div>
    <br />
    <div class="stat-desc" style="">
      <span style="font-weight: bolder">FIC</span> — Floor Impact Calculator, a
      stat created and maintained by Inpredictable. Floor Impact Counter aka FIC
      is a metric that is supposed to to fix flaws at PER, and PIE. Invented by
      the guys at RealGM, FIC weights more to assists, shot creation and
      offensive rebounding. Formula: (Points + ORB. + 0.75 DRB + AST + STL + BLK –0.75 FGA – 0.375 FTA – TO – 0.5 PF). To read more, visit
      <a href="https://basketball.realgm.com/info/glossary"
        >RealGM</a
      >.
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
about-container {
  min-height: 100vh;
}
div {
  color: white;
}

//Sass color variables
$link-color: lightblue;
$hover-color: darken($link-color, 20%);
$visited-color: darken($link-color, 10%);

//link styling
a {
  color: $link-color;
  text-decoration: none;

  &:hover {
    color: $hover-color;
    border-bottom: 1px solid $hover-color;
  }

  &:visited {
    color: $visited-color;
    border-color: $visited-color;
  }
}
</style>
