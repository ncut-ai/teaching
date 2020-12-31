jtrrouter -c simple6nodes.jtrrcfg.xml --accept-all-destinations

::jtrrouter --flow-files=test.flows.xml --turn-ratio-files=test.turns.xml --net-file=test.net.xml --output-file=test.rou.xml --begin 1 --end 1000
  
pause