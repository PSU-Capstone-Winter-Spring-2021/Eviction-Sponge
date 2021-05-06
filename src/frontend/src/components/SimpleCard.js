import React from 'react';
// import { makeStyles } from 'material-ui/core/styles';
import Card from '@material-ui/core/Card';
// import CardActions from 'material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
// import Button from 'material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import 'react-bootstrap';

export default class SimpleCard extends React.Component{
    constructor(props) {
                super(props);
                this.state = {
                    caseNum: Object.keys(this.props.res),
                    result: this.props.res
                  };
    }
    render (){
    const {caseNum} = this.state;
    const {location, style, status, eligibility, date} = this.state.result[caseNum];

    return(
    <div className = "bg-light">
        <Card className='bg-light border'>
        <CardContent>
            <Typography className={caseNum} color="textSecondary" gutterBottom>
            {caseNum} 
            </Typography>
            <Typography className={caseNum}  gutterBottom>
            Location: {location}
            </Typography>
            <Typography className={caseNum}  gutterBottom>
            Type: {style}
            </Typography>
            <Typography className={caseNum}  gutterBottom>
            status: {status}
            </Typography>
            <Typography variant="body2" component="p">
            date: {date}
            </Typography>
            <Typography variant="body2" component="p">
            eligibility: {eligibility}
            </Typography>
        </CardContent>
        </Card>
    </div>
    );
    }
}