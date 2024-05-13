import express from 'express';
import fetch from 'node-fetch';

import config from './util/configTreePath.js';
import { corsWithReady, liferayJWT, } from './util/liferay-oauth2-resource-server.js';
import {logger} from './util/logger.js';

const serverPort = config['server.port'];
const app = express();

logger.log(`config: ${JSON.stringify(config, null, '\t')}`);

app.use(express.json());
app.use(corsWithReady);
app.use(liferayJWT);

app.get(config.readyPath, (req, res) => { res.send('READY'); });

app.post('/sample/object/action/1', async (req, res) => {
	const json = req.body;

	const lxcDXPMainDomain = config['com.liferay.lxc.dxp.mainDomain'] || "localhost:8080";
	const lxcDXPServerProtocol = config['com.liferay.lxc.dxp.server.protocol'] || "http";

	liferayJWT(req,res,async ()=>{
		//WRITE YOUR CODE HERE
	});
	res.status(200).send(json);
});

app.listen(serverPort, () => { logger.log(`App listening on ${serverPort}`); });
export default app;
