import {
    IConfigurationExtend,
    IEnvironmentRead,
    IHttp,
    ILogger,
    IPersistence,
    IRead,
} from '@rocket.chat/apps-engine/definition/accessors';
import { App } from '@rocket.chat/apps-engine/definition/App';
import { IMessage, IPreMessageSentPrevent } from '@rocket.chat/apps-engine/definition/messages';
import { IAppInfo } from '@rocket.chat/apps-engine/definition/metadata';
import { SettingType } from '@rocket.chat/apps-engine/definition/settings';
import axios, { AxiosError, AxiosRequestConfig, AxiosResponse } from 'axios';

export class PhotoFilterApp extends App implements IPreMessageSentPrevent {
    constructor(info: IAppInfo, logger: ILogger) {
        super(info, logger);
    }

    public async checkPreMessageSentPrevent(message: IMessage, read: IRead, http: IHttp): Promise<boolean> {
        return true;
    }

    public async executePreMessageSentPrevent(message: IMessage, read: IRead, http: IHttp, persistence: IPersistence): Promise<boolean> {
        const imageUrl = (message.attachments || []).reduce((total, a) => {
                                return total + (a.imageUrl || '');
                            }, '');

        console.log('**************************  ' + imageUrl + '  **************************');
        const json = JSON.stringify({image_url: ['http://localhost:3000' + imageUrl]});
        console.log(json);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST', // or 'PUT'
            headers: {
                'Content-Type': 'application/json',
            },
            body: json,
            })
            .then((response) => response.json())
            .then((data) => {
            console.log('Success:----------------->>>>>>>>', data);
            })
            .catch((error) => {
            console.error('Error:', error);
            });

        read.getNotifier().notifyUser(message.sender, {
            room: message.room,
            sender: message.sender,
            text: 'Your message has been blocked by *Photo Filter*',
            alias: 'Content Filter',
            emoji: ':no_entry:',
        });

        return true;
    }
}
