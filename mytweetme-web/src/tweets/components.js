import React, { useEffect, useState } from 'react';
import { loadTweets } from '../lookup'


export function TweetsComponent(props) {
    const textAreaRef = React.createRef()
    const [newTweets, setNewTweets] = useState([])
    const handleSubmit = (event) => {
        event.preventDefault()
        const newValue = textAreaRef.current.value
        textAreaRef.current.value = ''
        let tempNewTweets = [...newTweets]
        tempNewTweets.unshift({
            content: newValue,
            likes: 0,
            id: 123123
        })
        setNewTweets(tempNewTweets)
    }
    return <div className={props.className}>
        <div className="col-12">

            <form onSubmit={handleSubmit}>
                <textarea required={true} ref={textAreaRef} className='form-control' name='tweet'>    </textarea>

                <button type="submit" className='btn btn-primary my-3'>Tweet</button>
            </form>
        </div>
        <TweetsList newTweets={newTweets} />
    </div>
}


export function TweetsList(props) {
    const [tweetsInit, setTweetsInit] = useState([])
    const [tweets, setTweets] = useState([])
    useEffect(() => {
        const final = [...props.newTweets].concat(tweetsInit)
        if (final.length !== tweets.length) {
            setTweets(final)
        }
    }, [props.newTweets, tweets, tweetsInit])

    useEffect(() => {
        const myCallback = (response, status) => {
            if (status === 200) {
                setTweetsInit(response)
            } else {
                alert("There as an error! oh no!")
            }
        }
        loadTweets(myCallback)
    }, [])
    return tweets.map((item, index) => {
        return <Tweet tweet={item} key={`${index}-{item.id}`} className='my-5 py-5 border bg-white text-dark' />
    })
}

export function ActionBtn(props) {
    const { tweet, action } = props
    const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0)
    const [userLike, setUserLike] = useState(false)
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'Action'
    const handleClick = (event) => {
        event.preventDefault()
        if (action.type === 'like') {
            if (userLike === true) {
                setLikes(likes - 1)
                setUserLike(false)
            } else {
                setLikes(tweet.likes + 1)
                setUserLike(true)
            }
        }
    }

    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
    return <button className={className} onClick={handleClick}>{display}</button>
}

export function Tweet(props) {
    const { tweet } = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{tweet.id} - {tweet.content}</p>
        <div className="btn btn-group">
            <ActionBtn tweet={tweet} action={{ type: "like", display: "Likes" }} />
            <ActionBtn tweet={tweet} action={{ type: "unlike", display: "unLikes" }} />
            <ActionBtn tweet={tweet} action={{ type: "reTweet", display: "reTweet" }} />
        </div>
    </div>
}
