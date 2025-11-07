package com.ms_agendamento.ms_agendamento;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.core.env.Environment;

import lombok.RequiredArgsConstructor;

@SpringBootApplication
public class MsAgendamentoApplication {

	public static void main(String[] args) {
		SpringApplication.run(MsAgendamentoApplication.class, args);
	}

}

@RequiredArgsConstructor
@RestController
@RequestMapping("/api/agendamentos")
class AgendamentoController {

	private final Environment environment;

	@GetMapping
	public String getAgendamentos() {
		String port = environment.getProperty("local.server.port");
		String hostname = "desconhecido";
		try {
			hostname = java.net.InetAddress.getLocalHost().getHostName();
		} catch (Exception ignored) {
		}

		return "Instância rodando na porta " + port + " | Host: " + hostname;
	}
}