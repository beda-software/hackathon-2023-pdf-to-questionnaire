import express from 'express';
import bodyParser from 'body-parser';
import fs from 'fs';
// @ts-ignore
import pdf2md from '@opendocsg/pdf2md';

const app = express();
const port = 8081;

// Middleware to parse incoming requests with binary data
app.use(bodyParser.raw({ type: 'application/octet-stream', limit: '10mb' }));

app.post('/', async (req: any, res: any) => {

  const markdown = await pdf2md(req.body);

  res.send(markdown);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
