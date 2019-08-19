import { Component } from '@angular/core';
import { ChatServiceService } from './chat-service.service';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'rasachatbot';
  response: any = [];
  formgroup: any = {};
  constructor(public rasaChat: ChatServiceService, private _formBuilder: FormBuilder) {

  }

  ngOnInit() {
    this.formgroup = this._formBuilder.group({
      chatbox: ['', Validators.required]
    })
  }

  onSubmit() {
    console.log(this.formgroup.value.chatbox)
    if (this.formgroup.value.chatbox) return
    let params = { "query": this.formgroup.value.chatbox }
    this.response.push({ person: 'me', msg: this.formgroup.value.chatbox })
    this.rasaChat.postInputs('conversations/atul/respond', params).subscribe((result: any) => {
      this.response.push({ person: 'him', msg: result[0].text });
      this.formgroup.patchValue({ chatbox: '' })
    })
  }



}
