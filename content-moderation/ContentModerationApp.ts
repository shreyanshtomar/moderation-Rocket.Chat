import {
    IHttp,
    ILogger,
    IPersistence,
    IRead,
} from '@rocket.chat/apps-engine/definition/accessors';
import { App } from '@rocket.chat/apps-engine/definition/App';
import { IMessage, IPreMessageSentPrevent } from '@rocket.chat/apps-engine/definition/messages';
import { IAppInfo } from '@rocket.chat/apps-engine/definition/metadata';

export class ContentModerationApp extends App implements IPreMessageSentPrevent {
    customLogger: ILogger;
    constructor(info: IAppInfo, logger: ILogger) {
        super(info, logger);
        this.customLogger = logger;
    }

    // public async checkPreMessageSentPrevent(message: IMessage, read: IRead, http: IHttp): Promise<boolean> {
    //     return true;
    // }

    public async executePreMessageSentPrevent(message: IMessage, read: IRead, http: IHttp, persistence: IPersistence): Promise<boolean> {
        // Grabbing image URLs..
        const serverUrl: string = 'http://localhost:5000/predict';
        const imageUrl = (message.attachments || []).map(a=>'http://host.docker.internal:3000' + a.imageUrl);

        if (imageUrl.length > 0) {
            console.log('****** ' + imageUrl + '  ******');
            const json = JSON.stringify({url: imageUrl});
            this.customLogger.log(json);
            //console.log(json);

            const options = {
                headers: {
                    'content-type': 'application/json',
                },
                content: json,
            };
            const response = await http.post(serverUrl, options);

            console.log(response.content);

            const imageObj = JSON.parse(response.content || '');

            if (imageObj.classification === 'nsfw') {
            read.getNotifier().notifyUser(message.sender, {
                room: message.room,
                sender: message.sender,
                text: 'Your message has been blocked by *Photo Filter* \nIf you think this is a false positive ask your administrator to turn off the app.',
                alias: 'Photos & Links Filter',
                emoji: ':no_entry:',
            });
            return true;
            }
        }

        // Grabbing links from text messages..
        const text = (message.text || '');
        const matches = text.match(/\bhttps?:\/\/\S+/gi);

        if (matches !== null) {
            const json = JSON.stringify({url: matches});
            console.log('****** ' + json + '****** ');
            const options = {
                headers: {
                    'content-type': 'application/json',
                },
                content: json,
            };
            const response = await http.post(serverUrl, options);
            console.log(response.content);
            const imageObj = JSON.parse(response.content || '');
            if (imageObj.classification === 'nsfw') {
            read.getNotifier().notifyUser(message.sender, {
                room: message.room,
                sender: message.sender,
                text: 'Your message has been blocked by *Photo Filter*. \nIf you think this is a false positive ask your administrator to turn off the app.',
                alias: 'Photos & Links Filter',
                emoji: ':no_entry:',
            });
            return true;
            }
        }
        return false;
      }
}
