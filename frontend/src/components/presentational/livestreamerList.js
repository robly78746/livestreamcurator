import React from 'react';
import TwitchStream from './twitchStream';

export default function LivestreamerList (props) {
    return (
        <div className="d-flex justify-content-around flex-wrap">
            {props.livestreams.map((streamInfo) => {
                return (
                    <TwitchStream channel={streamInfo.twitchUsername} key={streamInfo.name}/>
                );
            })}
        </div>
    );
}